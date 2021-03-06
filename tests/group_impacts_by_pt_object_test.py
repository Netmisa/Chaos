from nose.tools import *
from chaos import utils

class Obj(object):
    pass

def get_pt_object(uri, object_type):
    return {'name': uri}

def None_pt_object(uri, object_type):
    return {'name': None}

def test_impacts_by_pt_object_type():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'a'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)

    result = utils.group_impacts_by_pt_object(impacts, 'stop_area', None, get_pt_object)
    eq_(len(result), 3)

    eq_(result[0]['name'], 'a')
    eq_(result[1]['name'], 'b')
    eq_(result[2]['name'], 'c')

    result = utils.group_impacts_by_pt_object(impacts, 'network', None, get_pt_object)
    eq_(len(result), 1)
    eq_(result[0]['name'], 'c')


def test_impacts_by_pt_object_uri():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'a'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)

    result = utils.group_impacts_by_pt_object(impacts, None, 'a', get_pt_object)
    eq_(len(result), 1)
    eq_(result[0]['name'], 'a')

def test_impacts_by_pt_object_uris():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'a'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)
    uris = ['a', 'c']
    result = utils.group_impacts_by_pt_object(impacts, None, uris, get_pt_object)
    eq_(len(result), 2)
    eq_(result[0]['name'], 'a')
    eq_(result[1]['name'], 'c')

def test_impacts_by_pt_object_type_uri():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'a'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)

    result = utils.group_impacts_by_pt_object(impacts, 'stop_area', 'a', get_pt_object)
    eq_(len(result), 1)
    eq_(result[0]['name'], 'a')

def test_impacts_by_pt_object_type_uris():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'a'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    one_pt_object = Obj()
    one_pt_object.uri = 'c'
    one_pt_object.type='network'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)
    uris = ['a', 'c']
    result = utils.group_impacts_by_pt_object(impacts, 'stop_area', uris, get_pt_object)
    eq_(len(result), 2)
    eq_(result[0]['name'], 'a')
    eq_(result[1]['name'], 'c')

def test_impacts_pt_object_not_in_navitia():
    impacts = []
    one_impact = Obj()
    one_impact.id = '1'
    one_impact.objects = []
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    one_impact.objects.append(one_pt_object)

    impacts.append(one_impact)
    result = utils.group_impacts_by_pt_object(impacts, 'stop_area', ['b'], None_pt_object)
    eq_(len(result), 1)
    eq_(result[0]['name'], None)
