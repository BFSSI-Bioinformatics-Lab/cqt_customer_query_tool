from django.db import models
from django.utils import timezone
from django.urls import reverse
from pathlib import Path
from cqt_customer_query_tool.users.models import User
from simple_history.models import HistoricalRecords

STATUS_CHOICES = (
    ('IN_PROGRESS', 'In Progress'),
    ('WAITING_FOR_APPROVAL', 'Waiting for Approval'),
    ('COMPLETED', 'Completed')
)

PATHOGEN = (
    ('Campylobacter', 'Campylobacter'),
    ('Clostridium', 'Clostridium'),
    ('Cronobacter', 'Cronobacter'),
    ('Cyclospora', 'Cyclospora'),
    ('Escherichia coli', 'Escherichia coli'),
    ('Hepatitis', 'Hepatitis'),
    ('Listeria', 'Listeria'),
    ('Norovirus', 'Norovirus'),
    ('Salmonella', 'Salmonella'),
    ('Shigella', 'Shigella'),
    ('Vibrio', 'Vibrio'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

FOOD = (
    ('Poultry', 'Poultry'),
    ('Beef', 'Beef'),
    ('Pork', 'Pork'),
    ('Dairy', 'Dairy'),
    ('Eggs', 'Eggs'),
    ('Grains or baked', 'Grains or baked'),
    ('Ready-to-Eat', 'Ready-to-Eat'),
    ('Canned food', 'Canned food'),
    ('Frozen food', 'Frozen food'),
    ('Fish', 'Fish'),
    ('Seafood', 'Seafood'),
    ('Fruit', 'Fruit'),
    ('Vegetables', 'Vegetables'),
    ('Infant formula', 'Infant formula'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

CATEGORY = (
    ('Temperature (cooking, storage)', 'Temperature (cooking, storage)'),
    ('Regulations', 'Regulations'),
    ('Guidance', 'Guidance'),
    ('Micro criteria', 'Micro criteria'),
    ('Food handlers certificate', 'Food handlers certificate'),
    ('Leftovers', 'Leftovers'),
    ('Vulnerable populations', 'Vulnerable populations'),
    ('Dates (best before, expiry)', 'Dates (best before, expiry)'),
    ('Storage', 'Storage'),
    ('Catering', 'Catering'),
    ('Food handling', 'Food handling'),
    ('Spoilage', 'Spoilage'),
    ('Canning', 'Canning'),
    ('Not Applicable / Other', 'Not Applicable / Other')
)

class Query(models.Model):
    name = 'query'

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IN_PROGRESS')
    number_RDIMS = models.IntegerField(blank=True, null=True)
    
    date_input = models.DateTimeField(default=timezone.now)
    date_due = models.DateField(blank=True, null=True)
    date_BMH_received = models.DateField(blank=True, null=True)
    date_assigned_to_evaluator = models.DateField(blank=True, null=True)
    date_to_sections_head_for_approval = models.DateField(blank=True, null=True)
    date_to_customer = models.DateField(blank=True, null=True)
    
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    section_head = models.CharField(max_length=500, blank=True, null=True)
    # This is the same as evaluator
    # bmh_scientific_evaluator_lead = models.CharField(max_length=500, blank=True, null=True)
    name_of_requestor = models.CharField(max_length=500, blank=True, null=True)
    subject_line = models.TextField(null=True, blank=True)
    query_text = models.TextField(null=True, blank=True)
    query_response = models.TextField(null=True, blank=True)
    
    key_words = models.CharField(max_length=500, blank=True, null=True)
    pathogen = models.CharField(max_length=50, choices=PATHOGEN, default='Not Applicable / Other')
    food = models.CharField(max_length=50, choices=FOOD, default='Not Applicable / Other')
    category = models.CharField(max_length=50, choices=CATEGORY, default='Not Applicable / Other')
    
    affiliations = models.CharField(max_length=500, blank=True, null=True)
    query_redirected_to = models.CharField(max_length=500, blank=True, null=True)
    additiona_information = models.TextField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        app_label = "api"
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        return f"{self.id}: {self.title}"

    # How to find the url of any entry
    # def get_absolute_url(self):
    #     return reverse('entry_detail', kwargs={'pk': self.pk})
