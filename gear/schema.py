import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Gear


# class ClimberType(DjangoObjectType):
#     class Meta:
#         model = Climber
#
#
# class Query(ObjectType):
#     climber = graphene.Field(ClimberType, id=graphene.Int())
#     climbers = graphene.List(ClimberType)
#
#     def resolve_climber(self, info, id):
#         return Climber.objects.filter(id=id).first()
#
#     def resolve_climbers(self, info, **kwargs):
#         return Climber.objects.all()
#
#
# schema = graphene.Schema(query=Query)

class GearType(DjangoObjectType):
    class Meta:
        model = Gear


class Query(ObjectType):
    gear = graphene.Field(GearType)
