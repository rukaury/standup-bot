from datetime import datetime
from neomodel import (StructuredRel, StructuredNode, BooleanProperty, IntegerProperty, ZeroOrMore, StringProperty, UniqueIdProperty, RelationshipTo, Relationship, DateProperty, DoesNotExist, OneOrMore, One, RelationshipFrom, EmailProperty, Traversal, OUTGOING, FloatProperty, MultipleNodesReturned, ArrayProperty)

class BaseRel(StructuredRel):
    isToday = BooleanProperty(required=True)

class Task(StructuredNode):
    """
    Class to represent the School node
    """
    text = StringProperty(required=True)
    date = RelationshipTo("Date", 'TASK_WROTE_ON', cardinality=One, model=BaseRel)

class Date(StructuredNode):
    """
    Class to represent the Date node
    """
    date = DateProperty(default_now=False, format='%Y-%m-%d', unique=True)
    tasks = RelationshipFrom("Task", 'TASK_WROTE_ON', cardinality=ZeroOrMore, model=BaseRel)
    infos = RelationshipFrom("Info", 'INFO_WROTE_ON', cardinality=ZeroOrMore, model=BaseRel)

class Info(StructuredNode):
    """
    Class to represent the Date node
    """
    text = StringProperty(required=True)
    date = RelationshipTo("Date", 'INFO_WROTE_ON', cardinality=One)