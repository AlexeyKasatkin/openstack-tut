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


class ComputeZoneManager(base.Manager):
    resource_class = ComputeZone

    def create(self, name):
        """ """
        body = {'compute_zone': {'name': name}}
        return self._create('/os-computezones', body, 'compute_zone')

    def delete(self, name):
        """ """
        #body = {'compute_zone': {'name': name}}
        #self._delete('/os-computezones', body)
        self._delete('/os-computezones/%s' % name)

    def list(self):
        """ """
        return self._list('/os-computezones', 'compute_zones')

    def add_node(self, zone, node):
        """ """
        body = {'add_node': {'zone': zone, 'node': node}}
        return self._create("/os-computezones/%s/action" % zone,#base.getid(zone),
                            body, "compute_node_to_zone", return_raw=True)
        #return self._action('addNode', zone_id, {'node_id': node_id})

    def remove_node(self, zone, node):
        """ """
        body = {'remove_node': {'zone': zone, 'node': node}}
        return self._create("/os-computezones/%s/action" % zone,#base.getid(zone),
                            body, "compute_node_to_zone", return_raw=True)
        #return self._action('removeNode', zone_id, {'node_id': node_id})

    def list_nodes(self, zone):
        """ """
        body = {'list_nodes': None}#{'zone': zone}}
        return self._list("/os-computezones/%s/action" % zone,# base.getid(zone),
                          "compute_nodes", body=body)#, return_raw=True)
        #return self._action('listNodes', zone_id)

    # def _action(self, action, zone, **kwargs):
    #     """ """
    #     body = {action: None}#, "zone": zone}
    #     self.run_hooks('modify_body_for_action', body, **kwargs)
    #     url = '/os-computezones/%s/action' % zone
    #     #url = '/computezones/action'
    #     return self.api.client.post(url, body=body)
