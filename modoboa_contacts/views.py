"""Contacts views."""

from django.views import generic


class IndexView(generic.TemplateView):
    """Simple view to display index page."""

    template_name = "modoboa_contacts/index.html"

    def get_context_data(self, **kwargs):
        """Set menu selection."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context["selection"] = "contacts"
        return context
