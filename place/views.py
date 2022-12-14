from ast import Break, Not
import json
from persian import convert_en_numbers,convert_fa_numbers
from typing import Union, List, Type


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet, Model
from django.views import View
from django.db.models import ProtectedError
from device.models import DeviceInput
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

from device.views import EditCategory
from .models import Place, Branch
from .forms import PlaceForm, Branchform
from user.permissions import RegistrarPermission
from user.models import User


class EditPlace(LoginRequiredMixin,RegistrarPermission,View):

    place_id = None
    place = None

    def get(self, request):
        places = Place.objects.all()
        storekeepers=User.object.filter(role='storekeeper')
        print(storekeepers)
        return render(request, "place/form_edit_place.html", context={"places": places,'storekeepers':storekeepers})

    def load_data_ajax(request):
        EditPlace.place_id = request.GET.get("place_id")
        print(EditPlace.place_id)
        EditPlace.place: Place = get_object_or_404(Place, id=int(EditPlace.place_id))
        print(EditPlace.place)
        return JsonResponse(
            {"name": EditPlace.place.name, "boss": EditPlace.place.boss,'storekeeper':f'{EditPlace.place.storekeeper.first_name} {EditPlace.place.storekeeper.last_name}'}
        )

    def ajax_delete(request):
        place_id = request.GET.get("place_id")
        place: Place = get_object_or_404(Place, id=int(place_id))
        try:
            place.delete()
        except ProtectedError:
            return JsonResponse({"msg": "protectederror"})
        return JsonResponse({"msg": "success"})

    def obj_exists(self, name: str) -> bool:
        return Place.objects.filter(name=name).exists()

    def create(self, data: dict) -> json:
        if self.obj_exists(name=data["name"]):
            return JsonResponse({"msg": "exists"})
        Place.objects.create(**data)
        return JsonResponse({"msg": "success"})

    def update(self, data: dict) -> json:
        if EditPlace.place.name != data["name"] and \
            self.obj_exists(name=data["name"]):
            return JsonResponse({"msg": "exists"})
        # if EditPlace.place.boss != data["boss"] or EditPlace.place.storekeeper !=data['storekeeper']:
        #     if DeviceInput.objects.filter(place_id=EditPlace.place_id).exists():
        #         print('bbbbbbbbbbbbbbbbb')
        #         Place.objects.filter(id=EditPlace.place_id).update(update='update')
        #         place=Place.objects.create(**data)
        #         Branch.objects.filter(place_id=EditPlace.place_id).update(place=place)
        #     else:
        
        Place.objects.filter(id=EditPlace.place_id).update(**data)
        # Place.objects.filter(id=int(EditPlace.place_id)).update(**data)
        return JsonResponse({"msg": "success"})

    def post(self, request):
        form = PlaceForm(request.POST)
        print(form.errors)
        if form.is_valid():
            name=convert_fa_numbers(form.cleaned_data.get('name'))
            boss=convert_fa_numbers(form.cleaned_data.get('boss'))
            form.cleaned_data.update({'name':name,'boss':boss})
            if "form_add" in form.data:
                return self.create(data=form.cleaned_data)
            else:
                return self.update(data=form.cleaned_data)
        else:
            return JsonResponse({"msg": "error"})


class EditBranch(LoginRequiredMixin,RegistrarPermission,View):

    branch_id = None
    branch = None

    def get(self, request):
        """
        It gets all the branchs and places from the database and then renders the form_edit_branch.html
        template with the branchs and places as context
        
        :param request: The request object
        :return: A list of all the branchs and places in the database.
        """
        branchs = Branch.objects.all()
        places = Place.objects.all()
        context = {"branchs": branchs, "places": places}
        return render(request, "place/form_edit_branch.html", context=context)

    def obj_exists(self, data: dict) -> bool:
        """
        It checks if a branch exists in the database
        """
        return Branch.objects.filter(name=data["name"], place=data["place"]).exists()

    def create(self, data: dict) -> json:
        """
        It creates a new branch if the branch doesn't exist
        """
        if self.obj_exists(data):
            return JsonResponse({"msg": "exists"})
        Branch.objects.create(phone=convert_en_numbers(data.pop("phone")), **data)
        return JsonResponse({"msg": "success"})

    def update(self, data: dict) -> json:
        place_input :Union[QuerySet,list[Place]] = data["place"]
        print(EditBranch.branch["place"],'ggggggggggggg')
        place=Place.objects.values('id').get(id=EditBranch.branch["place"]) 
  
        if (EditBranch.branch['name'] != data["name"] \
            or place['id'] != place_input.id):
            if self.obj_exists(data):
                return JsonResponse({"msg": "exists"})
        # if EditBranch.branch['boss'] != data['boss']:
        #     if DeviceInput.objects.filter(branch_id=EditBranch.branch_id).exists():
        #         Branch.objects.filter(id=EditBranch.branch_id)
        #         self.create(data)   
        #         return JsonResponse({"msg": "success"})
        Branch.objects.filter(id=EditBranch.branch_id).update(**data)     
        return JsonResponse({"msg": "success"})

    def load_data_ajax(request):

        EditBranch.branch_id = request.GET.get("branch_id")
        EditBranch.branch: Branch = get_object_or_404(
            Branch, id=int(EditBranch.branch_id)
        )
        EditBranch.branch=Branch.objects.values('name','boss','place','phone').get(id=EditBranch.branch_id)
        return JsonResponse(EditBranch.branch)

    def ajax_delete(request):
        branch_id = request.GET.get("branch_id")
        branch: Branch = get_object_or_404(Branch, id=int(branch_id))
        try:
            branch.delete()
        except ProtectedError:
            return JsonResponse({"msg": "protectederror"})
        return JsonResponse({"msg": "success"})

    def post(self, request):
        form = Branchform(request.POST)
        if form.is_valid():
            form.cleaned_data.update(
                {
                    'name':convert_fa_numbers(form.cleaned_data.get('name')),
                    'boss':convert_fa_numbers(form.cleaned_data.get('boss'))
                }
            )
            print(form.cleaned_data)
            if "form_add" in form.data:
                return self.create(data=form.cleaned_data)
            else:
                return self.update(data=form.cleaned_data)
        else:
            return JsonResponse({"msg": "error"})
