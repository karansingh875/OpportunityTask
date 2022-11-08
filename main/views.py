from django.views.generic import UpdateView, CreateView, ListView
from main.models import Opportunity
from django.urls import reverse_lazy
from django.forms import DateInput, DateTimeInput, NumberInput


class OpportunityCreate(CreateView):
    """Create view for Opportunity."""
    model = Opportunity
    fields = "__all__"

    def get_context_data(self, *args, **kwargs):
        context = super(OpportunityCreate, self).get_context_data(
            *args, **kwargs)
        context['create'] = "create"
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(OpportunityCreate, self).get_form(form_class)
        form.fields['first_name'].widget.attrs = {
            "placeholder": "First Name",
            "class": "form-control form-control-lg"
        }
        form.fields['last_name'].widget.attrs = {
            "placeholder": "Last Name",
            "class": "form-control form-control-lg"
        }
        form.fields['address1'].widget.attrs = {
            "placeholder": "Address",
            "class": "form-control form-control-lg"
        }
        form.fields['address2'].widget.attrs = {
            "placeholder": "Address",
            "class": "form-control form-control-lg"
        }
        form.fields['city'].widget.attrs = {
            "placeholder": "City Name",
            "class": "form-control form-control-lg"}
        form.fields['postal_code'].widget = NumberInput(
            attrs={
                    "placeholder": "Postal Code",
                    "type": "number",
                    "pattern": "[0-9]{6}",
                    "class": "form-control form-control-lg"
                    })
        form.fields['phone_number1'].widget = NumberInput(attrs={
            "placeholder": "Phone Number (10 Digits)",
            "type": "tel",
            "pattern": "[0-9]{10}",
            "class": "form-control form-control-lg"
        })
        form.fields['phone_number2'].widget = NumberInput(attrs={
            "placeholder": "Phone Number (10 Digits)",
            "type": "tel",
            "pattern": "[0-9]{10}",
            "class": "form-control form-control-lg"
        })
        form.fields['sin'].widget = NumberInput(attrs={
            "placeholder": "Please Enter Sin (9 DIGITS)",
            "type": "tel",
            "pattern": "[0-9]{9}",
            "class": "form-control form-control-lg"
        })
        form.fields['email'].widget.attrs = {
            "placeholder": "email@example.com",
            "type": "email",
            "class": "form-control form-control-lg"
        }
        form.fields['agent'].widget.attrs = {
            "placeholder": "Agent Name here",
            "class": "form-control form-control-lg"
            }
        form.fields['collection_amount'].widget.attrs = {
            "placeholder": "Collection Amount",
            "class": "form-control form-control-lg"
        }
        form.fields['last_agent'].widget.attrs = {
            "placeholder": "Last Agent",
            "class": "form-control form-control-lg"
        }
        form.fields['collection_date'].widget.attrs = {
            "placeholder": "yyyy-mm-dd",
            "class": "form-control form-control-lg"
        }
        form.fields['last_crawl'].widget = DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control form-control-lg"
            })
        form.fields['dob'].widget = DateInput(
            attrs={
                "type": "date",
                "class": "form-control form-control-lg"
            })
        form.fields['last_result'].widget = DateInput(
            attrs={
                "type": "date",
                "class": "form-control form-control-lg"
                })
        form.fields["province"].widget.attrs = {
            "class": "form-select form-select-lg"
            }
        form.fields["prioritize_local"].widget.attrs = {
            "class": "form-select form-select-lg"
            }
        form.fields["prioritize_global"].widget.attrs = {
            "class": "form-select form-select-lg",
            }
        form.fields["file_upload"].widget.attrs = {
            "class": "form-control form-control-lg",
            "accept": ".doc, .docx, .pdf"
            }

        return form


class OpportunitySaveAndEditView(OpportunityCreate):

    """Save instance and redirect page to update that instance"""


class OpportunitySaveCreateNew(OpportunityCreate):

    """Create and redirect back to create form to create next"""

    success_url = reverse_lazy("main:opportunity_create")


class OpportunityCreateView(OpportunityCreate):

    """redirect to listview after creating."""

    success_url = reverse_lazy("opportunity_list")


class OpportunityUpdate(UpdateView):
    """Base update model for Opportunity"""
    model = Opportunity
    fields = "__all__"
    slug_field = "id"

    def get_context_data(self, *args, **kwargs):
        context = super(OpportunityUpdate, self).get_context_data(
            *args, **kwargs)
        context['update'] = "update"
        context["id"] = self.kwargs.get("pk")
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(OpportunityUpdate, self).get_form(form_class)
        form.fields['first_name'].widget.attrs = {
            "placeholder": "First Name",
            "class": "form-control form-control-lg"
        }
        form.fields['last_name'].widget.attrs = {
            "placeholder": "Last Name",
            "class": "form-control form-control-lg"
        }
        form.fields['address1'].widget.attrs = {
            "placeholder": "Address",
            "class": "form-control form-control-lg"
        }
        form.fields['address2'].widget.attrs = {
            "placeholder": "Address",
            "class": "form-control form-control-lg"
        }
        form.fields['city'].widget.attrs = {
            "placeholder": "City Name",
            "class": "form-control form-control-lg"}
        form.fields['postal_code'].widget = NumberInput(
            attrs={
                    "placeholder": "Postal Code",
                    "type": "number",
                    "pattern": "[0-9]{6}",
                    "class": "form-control form-control-lg",
                    })
        form.fields['phone_number1'].widget = NumberInput(attrs={
            "placeholder": "Phone Number (10 Digits)",
            "type": "tel",
            "pattern": "[0-9]{10}",
            "class": "form-control form-control-lg"
        })
        form.fields['phone_number2'].widget = NumberInput(attrs={
            "placeholder": "Phone Number (10 Digits)",
            "type": "tel",
            "pattern": "[0-9]{10}",
            "class": "form-control form-control-lg"
        })
        form.fields['sin'].widget = NumberInput(attrs={
            "placeholder": "Please Enter Sin (9 DIGITS)",
            "type": "tel",
            "pattern": "[0-9]{9}",
            "class": "form-control form-control-lg"
        })
        form.fields['email'].widget.attrs = {
            "placeholder": "email@example.com",
            "type": "email",
            "class": "form-control form-control-lg"
        }
        form.fields['agent'].widget.attrs = {
            "placeholder": "Agent Name here",
            "class": "form-control form-control-lg"
            }
        form.fields['collection_amount'].widget.attrs = {
            "placeholder": "Collection Amount",
            "class": "form-control form-control-lg"
        }
        form.fields['last_agent'].widget.attrs = {
            "placeholder": "Last Agent",
            "class": "form-control form-control-lg"
        }
        form.fields['collection_date'].widget.attrs = {
            "placeholder": "yyyy-mm-dd",
            "class": "form-control form-control-lg"
        }
        form.fields['last_crawl'].widget = DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control form-control-lg"
            })
        form.fields['dob'].widget = DateInput(
            attrs={
                "type": "date",
                "class": "form-control form-control-lg"
            })
        form.fields['last_result'].widget = DateInput(
            attrs={
                "type": "date",
                "class": "form-control form-control-lg"
                })
        form.fields["province"].widget.attrs = {
            "class": "form-select form-select-lg"
            }
        form.fields["prioritize_local"].widget.attrs = {
            "class": "form-select form-select-lg"
            }
        form.fields["prioritize_global"].widget.attrs = {
            "class": "form-select form-select-lg",
            }
        form.fields["file_upload"].widget.attrs = {
            "class": "form-control form-control-lg",
            "accept": ".doc, .docx, .pdf"
            }

        return form


class OpportunityUpdateView(OpportunityUpdate):

    """Updating individual opportunities."""

    success_url = reverse_lazy("opportunity_list")


class OpportunityUpdateListView(OpportunityUpdate):

    """Updating individual opportunities."""

    success_url = reverse_lazy("opportunity_list")


class OpportunityUpdateEdit(OpportunityUpdate):

    """Update and redirect to edit the form."""


class OpportunityUpdateCreateView(OpportunityUpdate):
    """View to save updated data and redirect user to add new data"""

    success_url = reverse_lazy("main:opportunity_create")


class OpportunityListView(ListView):

    """Return all the list of added items."""

    model = Opportunity
