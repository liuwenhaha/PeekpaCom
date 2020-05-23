from django import forms
from apps.base.forms import FormMixin
from apps.poster.models import Category, Tag, Post
from apps.exchangelink.models import ExchangeLink
from apps.basefunction.models import NavbarItem
from apps.datacenter.models import Code


class CategoryForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryEditForm(forms.ModelForm, FormMixin):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = Category
        fields = "__all__"


class TagForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Tag
        fields = "__all__"


class TagEditForm(forms.ModelForm, FormMixin):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = Tag
        fields = "__all__"


class PostForm(forms.ModelForm, FormMixin):
    tag_id = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())

    class Meta:
        model = Post
        exclude = ('tag',)


class PostEditForm(forms.ModelForm, FormMixin):
    tag_id = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())
    id = forms.CharField(max_length=100)
    class Meta:
        model = Post
        exclude = ('tag',)


class ExchangeLinkForm(forms.ModelForm, FormMixin):
    class Meta:
        model = ExchangeLink
        fields = "__all__"


class ExchangeLinkEditForm(forms.ModelForm, FormMixin):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = ExchangeLink
        fields = "__all__"


class NavItemForm(forms.ModelForm, FormMixin):
    class Meta:
        model = NavbarItem
        fields = "__all__"


class NavItemEditForm(forms.ModelForm, FormMixin):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = NavbarItem
        fields = "__all__"


class CodeForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Code
        exclude = ('visit_num',)


class CodeEditForm(forms.ModelForm, FormMixin):
    pk = forms.CharField(max_length=100)

    class Meta:
        model = Code
        exclude = ('visit_num',)

