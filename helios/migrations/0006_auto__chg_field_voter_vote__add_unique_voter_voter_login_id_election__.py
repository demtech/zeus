# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Voter.vote'
        db.alter_column('helios_voter', 'vote', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Adding unique constraint on 'Voter', fields ['voter_login_id', 'election']
        db.create_unique('helios_voter', ['voter_login_id', 'election_id'])

        # Changing field 'Election.result'
        db.alter_column('helios_election', 'result', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Election.questions'
        db.alter_column('helios_election', 'questions', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Election.encrypted_tally'
        db.alter_column('helios_election', 'encrypted_tally', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Election.eligibility'
        db.alter_column('helios_election', 'eligibility', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Election.private_key'
        db.alter_column('helios_election', 'private_key', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Election.public_key'
        db.alter_column('helios_election', 'public_key', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Trustee.public_key'
        db.alter_column('helios_trustee', 'public_key', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Trustee.decryption_proofs'
        db.alter_column('helios_trustee', 'decryption_proofs', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Trustee.pok'
        db.alter_column('helios_trustee', 'pok', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Trustee.secret_key'
        db.alter_column('helios_trustee', 'secret_key', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'Trustee.decryption_factors'
        db.alter_column('helios_trustee', 'decryption_factors', self.gf('helios.datatypes.djangofield.LDObjectField')(null=True))

        # Changing field 'CastVote.vote'
        db.alter_column('helios_castvote', 'vote', self.gf('helios.datatypes.djangofield.LDObjectField')())


    def backwards(self, orm):
        
        # Removing unique constraint on 'Voter', fields ['voter_login_id', 'election']
        db.delete_unique('helios_voter', ['voter_login_id', 'election_id'])

        # Changing field 'Voter.vote'
        db.alter_column('helios_voter', 'vote', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.result'
        db.alter_column('helios_election', 'result', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.questions'
        db.alter_column('helios_election', 'questions', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.encrypted_tally'
        db.alter_column('helios_election', 'encrypted_tally', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.eligibility'
        db.alter_column('helios_election', 'eligibility', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.private_key'
        db.alter_column('helios_election', 'private_key', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Election.public_key'
        db.alter_column('helios_election', 'public_key', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Trustee.public_key'
        db.alter_column('helios_trustee', 'public_key', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Trustee.decryption_proofs'
        db.alter_column('helios_trustee', 'decryption_proofs', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Trustee.pok'
        db.alter_column('helios_trustee', 'pok', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Trustee.secret_key'
        db.alter_column('helios_trustee', 'secret_key', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'Trustee.decryption_factors'
        db.alter_column('helios_trustee', 'decryption_factors', self.gf('heliosauth.jsonfield.JSONField')(null=True))

        # Changing field 'CastVote.vote'
        db.alter_column('helios_castvote', 'vote', self.gf('heliosauth.jsonfield.JSONField')())


    models = {
        'heliosauth.user': {
            'Meta': {'unique_together': "(('user_type', 'user_id'),)", 'object_name': 'User'},
            'admin_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('heliosauth.jsonfield.JSONField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'token': ('heliosauth.jsonfield.JSONField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'helios.auditedballot': {
            'Meta': {'object_name': 'AuditedBallot'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_vote': ('django.db.models.fields.TextField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'helios.castvote': {
            'Meta': {'object_name': 'CastVote'},
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalidated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'quarantined_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'released_from_quarantine_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'verified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'vote': ('helios.datatypes.djangofield.LDObjectField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vote_tinyhash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Voter']"})
        },
        'helios.election': {
            'Meta': {'object_name': 'Election'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heliosauth.User']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'cast_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'complaint_period_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datatype': ('django.db.models.fields.CharField', [], {'default': "'legacy/Election'", 'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'election_type': ('django.db.models.fields.CharField', [], {'default': "'election'", 'max_length': '250'}),
            'eligibility': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'encrypted_tally': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'featured_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frozen_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'openreg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'private_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'private_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'questions': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'registration_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'result': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'result_proof': ('heliosauth.jsonfield.JSONField', [], {'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tallies_combined_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_finished_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'use_advanced_audit_features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_voter_aliases': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'voters_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voting_ended_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_extended_until': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        'helios.electionlog': {
            'Meta': {'object_name': 'ElectionLog'},
            'at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'helios.trustee': {
            'Meta': {'object_name': 'Trustee'},
            'decryption_factors': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'decryption_proofs': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pok': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'public_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'public_key_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'helios.voter': {
            'Meta': {'unique_together': "(('election', 'voter_login_id'),)", 'object_name': 'Voter'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heliosauth.User']", 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'voter_login_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'voter_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'helios.voterfile': {
            'Meta': {'object_name': 'VoterFile'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_voters': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'processing_finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'processing_started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'voter_file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['helios']
