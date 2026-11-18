
import uuid
from django.db import models


class Account(models.Model):
    """
    Hospital financial account.
    ERD: accounts
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    name = models.TextField()
    account_type = models.TextField()
    account_number = models.TextField()

    opening_balance = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )

    is_active = models.BooleanField()

    class Meta:
        db_table = "accounts"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_accounts_hospital_id_id"
            )
        ]


class IncomeCategory(models.Model):
    """
    Hospital income categories.
    ERD: income_categories
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    department_id = models.UUIDField(
        null=True,
        blank=True
    )

    name = models.TextField()

    class Meta:
        db_table = "income_categories"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_income_cat_hospital_id"
            )
        ]


class ExpenseCategory(models.Model):
    """
    Hospital expense categories.
    ERD: expense_categories
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    name = models.TextField()

    class Meta:
        db_table = "expense_categories"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "name"],
                name="uq_exp_cat_hospital_name"
            ),
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_exp_cat_hospital_id"
            )
        ]


class Invoice(models.Model):
    """
    Patient billing invoice.
    ERD: invoices
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    patient_id = models.UUIDField(
        null=True,
        blank=True
    )

    patient_visit_id = models.UUIDField(
        null=True,
        blank=True
    )

    created_by_hospital_user_id = models.UUIDField()

    invoice_number = models.TextField()

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.TextField()
    issued_at = models.DateTimeField()

    class Meta:
        db_table = "invoices"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_invoice_hospital_id"
            )
        ]


class InvoiceItem(models.Model):
    """
    Individual services or products in an invoice.
    ERD: invoice_items
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.DO_NOTHING,
        db_column="invoice_id",
        related_name="items"
    )

    department_id = models.UUIDField()

    appointment_id = models.UUIDField(
        null=True,
        blank=True
    )

    test_order_item_id = models.UUIDField(
        null=True,
        blank=True
    )

    medicine_sale_item_id = models.UUIDField(
        null=True,
        blank=True
    )

    blood_issue_id = models.UUIDField(
        null=True,
        blank=True
    )

    emergency_case_id = models.UUIDField(
        null=True,
        blank=True
    )

    description = models.TextField()

    quantity = models.IntegerField()

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    line_total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.TextField()

    class Meta:
        db_table = "invoice_items"
        constraints = [
            models.CheckConstraint(
                condition=(
                    (
                        models.Q(appointment_id__isnull=True)
                        | models.Q(test_order_item_id__isnull=True)
                    )
                    & (
                        models.Q(appointment_id__isnull=True)
                        | models.Q(medicine_sale_item_id__isnull=True)
                    )
                    & (
                        models.Q(appointment_id__isnull=True)
                        | models.Q(blood_issue_id__isnull=True)
                    )
                    & (
                        models.Q(appointment_id__isnull=True)
                        | models.Q(emergency_case_id__isnull=True)
                    )
                    & (
                        models.Q(test_order_item_id__isnull=True)
                        | models.Q(medicine_sale_item_id__isnull=True)
                    )
                    & (
                        models.Q(test_order_item_id__isnull=True)
                        | models.Q(blood_issue_id__isnull=True)
                    )
                    & (
                        models.Q(test_order_item_id__isnull=True)
                        | models.Q(emergency_case_id__isnull=True)
                    )
                    & (
                        models.Q(medicine_sale_item_id__isnull=True)
                        | models.Q(blood_issue_id__isnull=True)
                    )
                    & (
                        models.Q(medicine_sale_item_id__isnull=True)
                        | models.Q(emergency_case_id__isnull=True)
                    )
                    & (
                        models.Q(blood_issue_id__isnull=True)
                        | models.Q(emergency_case_id__isnull=True)
                    )
                ),
                name="ck_invoice_item_one_source"
            ),

            models.UniqueConstraint(
                fields=["appointment_id"],
                condition=models.Q(
                    status="active",
                    appointment_id__isnull=False
                ),
                name="uq_inv_item_appt_active"
            ),

            models.UniqueConstraint(
                fields=["test_order_item_id"],
                condition=models.Q(
                    status="active",
                    test_order_item_id__isnull=False
                ),
                name="uq_inv_item_test_active"
            ),

            models.UniqueConstraint(
                fields=["medicine_sale_item_id"],
                condition=models.Q(
                    status="active",
                    medicine_sale_item_id__isnull=False
                ),
                name="uq_inv_item_medicine_active"
            ),

            models.UniqueConstraint(
                fields=["blood_issue_id"],
                condition=models.Q(
                    status="active",
                    blood_issue_id__isnull=False
                ),
                name="uq_inv_item_blood_active"
            )
        ]


class Payment(models.Model):
    """
    Patient invoice payments and refunds.
    ERD: payments
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.DO_NOTHING,
        db_column="invoice_id",
        related_name="payments"
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.DO_NOTHING,
        db_column="account_id",
        related_name="payments"
    )

    received_by_hospital_user_id = models.UUIDField()

    refunded_payment = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="refunded_payment_id",
        related_name="refunds"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    method = models.TextField()
    kind = models.TextField()
    status = models.TextField()

    reference_no = models.TextField()

    paid_at = models.DateTimeField()

    class Meta:
        db_table = "payments"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_payment_hospital_id"
            )
        ]


class Expense(models.Model):
    """
    Hospital expenditure records.
    ERD: expenses
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    expense_category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.DO_NOTHING,
        db_column="expense_category_id",
        related_name="expenses"
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.DO_NOTHING,
        db_column="account_id",
        related_name="expenses"
    )

    supplier_id = models.UUIDField(
        null=True,
        blank=True
    )

    approved_by_hospital_user_id = models.UUIDField(
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    expense_date = models.DateField()

    description = models.TextField()

    status = models.TextField()

    class Meta:
        db_table = "expenses"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_expense_hospital_id"
            )
        ]


class Transaction(models.Model):
    """
    Hospital financial transaction ledger.
    ERD: transactions (append-only)
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    hospital_id = models.UUIDField(db_index=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.DO_NOTHING,
        db_column="account_id",
        related_name="transactions"
    )

    income_category = models.ForeignKey(
        IncomeCategory,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="income_category_id",
        related_name="transactions"
    )

    expense_category = models.ForeignKey(
        ExpenseCategory,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="expense_category_id",
        related_name="transactions"
    )

    payment = models.OneToOneField(
        Payment,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="payment_id",
        related_name="transaction"
    )

    expense = models.OneToOneField(
        Expense,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="expense_id",
        related_name="transaction"
    )

    reversed_transaction = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        db_column="reversed_transaction_id",
        related_name="reversal_transactions"
    )

    transaction_type = models.TextField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    transaction_date = models.DateField()

    description = models.TextField()

    class Meta:
        db_table = "transactions"
        constraints = [
            models.UniqueConstraint(
                fields=["hospital_id", "id"],
                name="uq_transaction_hospital_id"
            )
        ]
