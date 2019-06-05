import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Gear


class GearType(DjangoObjectType):
    class Meta:
        model = Gear


class Query(ObjectType):
    gear = graphene.Field(GearType, id=graphene.Int())
    gears = graphene.List(GearType)

    def resolve_gear(self, info, gear_id):
        return Gear.objects.filter(id=gear_id).first()

    def resolve_gears(self, info, **kwargs):
        return Gear.objects.all()


schema = graphene.Schema(query=Query)
