from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Categories
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from django.db import IntegrityError


def get_children_for_post(children, parent_category):
    for category in children:
        if 'name' in category:
            try:
                category_obj_name = category['name']
                parent_category_new = Category(name=category_obj_name)
                parent_category_new.save()
                parent_category.category_obj.children.add(parent_category_new)
            except IntegrityError as e:
                response = f"{e}:category with this name already exists"
                return Response(data=response)
        if 'children' in category:
            children = category['children']
            get_children_for_post(children, parent_category_new)


def get_parents(category):
    parents = Categories.objects.filter(children=category)
    for parent in parents:

        if parent:
            category_serializer = CategorySerializer(parent.category)

            if category_serializer.data not in response_parents:
                response_parents.append(category_serializer.data)
            get_parents(parent.category)

    return response_parents


def get_children(category):
    response_children = []
    parent = Categories.objects.get(category=category)
    children = parent.children.all()

    for child in children:
        if child:
            category_serializer = CategorySerializer(child)
            response_children.append(category_serializer.data)

    return response_children


def get_siblings(category):
    response_siblings = []
    try:
        parent = Categories.objects.get(children=category)
        children = parent.children.all()

        for child in children:

            if child.id is not category.id:

                category_serializer = CategorySerializer(child)
                response_siblings.append(category_serializer.data)

        return response_siblings
    except Categories.DoesNotExist:
        return response_siblings


class CategoriesView(APIView):

    def post(self, request):
        post_data = request.data
        response = post_data
        try:
            category_obj = request.data.get('name')
            parent_category = Category(name=category_obj)
            parent_category.save()
            children = request.data.get('children')
            if children:
                get_children_for_post(children, parent_category)
        except IntegrityError as e:
            response = f"{e}: category with this name already exists"

        return Response(data=response)


class CategoriesGetView(APIView):
    def get(self, request, id):
        global response_parents
        response_parents = []
        category = get_object_or_404(Category, pk=id)

        if category:
            response_childrens = get_children(category)
            response_parents = get_parents(category)
            response_siblings = get_siblings(category)
            category_serializer = CategorySerializer(category)
            category_dictionary = category_serializer.data
            category_dictionary['parents'] = response_parents
            category_dictionary['children'] = response_childrens
            category_dictionary['siblings'] = response_siblings
            return Response(data=category_dictionary)
        else:
            return Response(data="No category exist with given id")
