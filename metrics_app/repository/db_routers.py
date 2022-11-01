#!/usr/bin/env python
from django.db import models

class AppRouter:
	""" 
	A router to control all database operations on models in each clinical 
	study app.
	It is very important to specify 'app':'database' in route_app_labels where 'app' is name of app and 'database' is name 
	of database specified in the settings.py file for the project, this is true for all apps except search which uses the 
	default database which is for the repository
	"""

	route_app_labels = {'ihab':'ihab','rvpsyndromic':'rvpsyndromic'}
	route_app_label = {'ihab','rvpsyndromic'}

	def db_for_read(self, model, **hints):
		"""
		Attempts to read app models go to relevant db
		"""
		if model._meta.app_label in self.route_app_labels:
			return self.route_app_labels[model._meta.app_label]
		#if model._meta.app_label in self.route_app_label:
		#	return 'ihab' 
		return None

	def db_for_write(self, model, **hints):
		"""
		Attempts to read app models go to relevant db
		"""
		if model._meta.app_label in self.route_app_labels:
			return self.route_app_labels[model._meta.app_label]
		#if model._meta.app_label in self.route_app_label:
		#	return 'ihab' 
		return None

	def allow_relation(self, obj1, obj2, **hints):
		"""
		Allow relations if a model is in route_app_labels
		"""
		if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
			return True 
		#if (obj1._meta.app_label in self.route_app_label or obj2._meta.app_label in self.route_app_label):
		#	return True 
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""
		Attempts to read app models go to relevant db
		"""
		if app_label in self.route_app_labels:
			return db == self.route_app_labels[app_label]
		#if app_label in self.route_app_label:
		#	return 'ihab' 
		return None
