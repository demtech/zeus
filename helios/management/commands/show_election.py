"""
"""
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.timesince import timesince

from helios import utils as helios_utils
from helios.models import *

class Command(BaseCommand):
    args = ''
    help = 'Show election status'

    def handle(self, *args, **options):
        if not args:
            now = datetime.datetime.now()
            args = Election.objects.filter(voting_starts_at__lt=now, voting_ends_at__gt=now)
            args = args.values_list('uuid', flat=True)

        for uuid in args:
            election = Election.objects.get(uuid=uuid)

            frozen_at = election.frozen_at
            starts_at = election.voting_starts_at
            started_at = election.voting_started_at
            ends_at = election.voting_ends_at
            extended_until = election.voting_extended_until
            ended_at = election.voting_ended_at
            canceled_at = election.canceled_at
            last_visit_at = election.last_voter_visit()
            if last_visit_at is not None:
                last_visit_text = last_visit_at.strftime("%Y-%m-%d %H:%M:%S") + \
                        " (%s ago)" % (timesince(last_visit_at))
            else:
                last_visit_text = 'none'

            print "uuid:                 ", election.uuid
            print "admin:                ", election.admins.all()[0].pretty_name
            print "name:                 ", election.name
            print "institution:          ", election.institution.name
            print "frozen_at:            ", frozen_at and frozen_at.strftime("%Y-%m-%d %H:%M:%S")
            print "voting_starts_at:     ", starts_at and starts_at.strftime("%Y-%m-%d %H:%M:%S")
            print "voting_started_at:    ", started_at and started_at.strftime("%Y-%m-%d %H:%M:%S")
            print "voting_ends_at:       ", ends_at and ends_at.strftime("%Y-%m-%d %H:%M:%S")
            print "voting_extended_until:", extended_until and extended_until.strftime("%Y-%m-%d %H:%M:%S")
            print "voting_ended_at:      ", ended_at and ended_at.strftime("%Y-%m-%d %H:%M:%S")
            print "canceled_at:          ", canceled_at and canceled_at.strftime("%Y-%m-%d %H:%M:%S")
            print "voters:               ", election.voter_set.count()
            print "counted votes:         %d/%d" % (election.voted_count(), election.castvote_set.count())
            print "voters visits:        ", election.voters_visited_count()
            print "last voter visit:     ", last_visit_text
            print ""

