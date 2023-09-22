import graphene

from graphene_django import DjangoObjectType

from .models import Skills, Profile

class SkillsType(DjangoObjectType):
    class Meta:
        model=Skills
        fields=("id","list","techstack")
        


class ProfileType(DjangoObjectType):
    class Meta:
        model=Profile
        fields=("id","name","role","skills")

class Query(graphene.ObjectType):
    all_profiles=graphene.List(ProfileType)

    def resolve_all_profiles(root,info):
        return Profile.objects.all()
    

schema = graphene.Schema(query=Query)
