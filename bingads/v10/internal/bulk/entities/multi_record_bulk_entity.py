from abc import ABCMeta, abstractproperty
from future.utils import with_metaclass
from bingads.v10.bulk.entities.bulk_entity import BulkEntity


class _MultiRecordBulkEntity(with_metaclass(ABCMeta, BulkEntity)):
    """ Bulk entity that has its data in multiple records within the bulk file.

    For example, :class:`.BulkSiteLinkAdExtension` is a multi record bulk entity which can contain one or more
    :class:`.BulkSiteLink` child entities, which are themselves derived from :class:`.SingleRecordBulkEntity`.

    For more information, see Bulk File Schema at http://go.microsoft.com/fwlink/?LinkID=620269.
    """

    def __init__(self):
        super(_MultiRecordBulkEntity, self).__init__()

    @abstractproperty
    def child_entities(self):
        """ The child entities that this multi record entity contains.

        :rtype: list[BulkEntity]
        """

        raise NotImplementedError()

    @abstractproperty
    def all_children_are_present(self):
        """ True, if the object is fully constructed (contains all of its children), determined by the presence of delete all row, False otherwise

        :rtype: bool
        """

        raise NotImplementedError()

    @property
    def has_errors(self):
        """ Indicates whether or not the errors property of any of the ChildEntities is null or empty.

        If true, one or more ChildEntities contains the details of one or more :class:`.BulkError` objects.

        :rtype: bool
        """

        return any([x.has_errors for x in self.child_entities])

    @property
    def last_modified_time(self):
        """ Gets the last modified time for the first child entity, or null if there are no ChildEntities.

        :rtype: datetime.datetime
        """

        return self.child_entities[0].last_modified_time if self.child_entities else None

    @property
    def can_enclose_in_multiline_entity(self):
        return super(_MultiRecordBulkEntity, self).can_enclose_in_multiline_entity

    def enclose_in_multiline_entity(self):
        return super(_MultiRecordBulkEntity, self).enclose_in_multiline_entity()

    def read_from_row_values(self, row_values):
        super(_MultiRecordBulkEntity, self).read_from_row_values(row_values)

    def write_to_row_values(self, row_values):
        super(_MultiRecordBulkEntity, self).write_to_row_values(row_values)
