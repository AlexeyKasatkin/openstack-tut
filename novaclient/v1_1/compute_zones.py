# Copyright 2011 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Compute zones interface (1.1 extension).
"""

from novaclient import base


class ComputeZone(base.Resource):
    """
    Compute zone is an additional entity that can dynamically aggregate
    compute nodes by some name (name of zone).
    Relation between compute zones and compute nodes - many to many.
    """

    def __repr__(self):
        return "<ComputeZone: %s>" % self.id

    def delete(self):
        self.manager.delete(self)


class ComputeZoneManager(base.ManagerWithFind):
    resource_class = ComputeZone

    def create(self, name):
        """ """
        body = {'compute_zone': {'name': name}}
        return self._create('/os-computezones', body, 'compute_zone')

    def delete(self, name):
        """ """
        self._delete('/os-computezones/%s' % name)

    def list(self):
        """ """
        return self._list('/os-computezones', 'compute_zones')

    def add_node(self, zone_id, node_id):
        """ """
        body = {'nodetozone': {'zone_id': zone_id, 'node_id': node_id} }
        return self._add_node('/os-computezones', body, 'compute_zone')

    def remove_node(self, zone_id, node_id):
        """ """
        body = {'nodetozone': {'zone_id': zone_id, 'node_id': node_id} }
        return self._remove_node('/os-computezones', body)

    def list_nodes(self, zone_id):
        """ """
        body = {'computezone': {'zone_id': zone_id}}
        return self._list_nodes('/os-computezones', body)