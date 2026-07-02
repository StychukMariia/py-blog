from django import forms
from .models import Commentary


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]

    def clean(self):
        cleaned_data = super().clean()
        if not self.initial.get("user").is_authenticated:
            raise forms.ValidationError(
                "Only authorized users can post comments"
            )
        return cleaned_data
