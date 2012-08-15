# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns(
    'geocamTiePoint.views',

    url(r'^overlay/$', 'overlayIndex',
        {}, 'geocamTiePoint_overlayIndex'),

    url(r'^overlay/new/$', 'overlayNew',
        {}, 'geocamTiePoint_overlayNew'),

    url(r'^overlay/(?P<key>\d+)/$', 'overlayId',
        {}, 'geocamTiePoint_overlayId'),

    url(r'^overlay/(?P<key>\d+).json$', 'overlayIdJson',
        {}, 'geocamTiePoint_overlayIdJson'),

    url(r'^overlay/(?P<key>\d+)/warp/$', 'overlayIdWarp',
        {}, 'geocamTiePoint_overlayIdWarp'),

    url(r'^overlay/(?P<key>\d+)/delete/$', 'overlayDelete',
        {}, 'geocamTiePoint_overlayDelete'),

    url(r'^overlay/(?P<key>\d+)/preview/$', 'overlayIdPreview',
        {}, 'geocamTiePoint_overlayIdPreview'),

    url(r'^overlay/(?P<key>\d+)/(?P<fileName>\S+)$',
        'overlayIdImageFileName',
        {}, 'geocamTiePoint_overlayIdImageFileName'),

    url(r'^tile/(?P<quadTreeId>\d+)/$',
        'dummyView',
        {}, 'geocamTiePoint_tileRoot'),

    url(r'^tile/(?P<quadTreeId>\d+)/(?P<zoom>\d+)/(?P<x>\d+)/(?P<y>\d+)\.(\w+)$',
        'getTile',
        {}, 'geocamTiePoint_tile'),

    url(r'^ember/$', 'ember',
        {}, 'geocamTiePoint_ember'),
)
