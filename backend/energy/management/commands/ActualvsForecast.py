from django.core.management.base import BaseCommand, CommandError
from energy.models import *
from django.db.models import Sum
from django.db.models import F
from itertools import zip_longest

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--area', type=str)
        parser.add_argument('--timeres', type=str)
        parser.add_argument('--date',  type=str)
        parser.add_argument('--month', type=str)
        parser.add_argument('--year', type=str)

    def handle(self, *args, **options):
        area = options['area']
        timeres = options['timeres']
        r = Resolutioncode.objects.get(resolutioncodetext=timeres)
        if options['date']:
          date = options['date']
          s = date.split('-')
          l1 = Actualtotalload.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), day=int(s[2]), resolutioncodeid=r.id).annotate(realtotalload=F('totalloadvalue')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'realtotalload')
          l2 = Dayaheadtotalloadforecast.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), day=int(s[2]), resolutioncodeid=r.id).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue')
          l3 = [{**u, **v} for u, v in zip(l1, l2)]
        elif options['month']:
          month=options['month']
          s = month.split('-')
          l1 = Actualtotalload.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), resolutioncodeid=r.id).annotate(realtotalload=F('totalloadvalue')).annotate(realtotalload=Sum('realtotalload')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'realtotalload')
          l2 = Dayaheadtotalloadforecast.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), resolutioncodeid=r.id).annotate(totalload=Sum('totalloadvalue')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue')
          l3 = [{**u, **v} for u, v in zip(l1, l2)]
        elif options['year']:
          l1 = Actualtotalload.objects.filter(areaname=area, year=int(options['year']), resolutioncodeid=r.id).annotate(realtotalload=F('totalloadvalue')).annotate(realtotalload=Sum('realtotalload')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'datetime', 'realtotalload')
          l2 = Dayaheadtotalloadforecast.objects.filter(areaname=area, year=int(options['year']), resolutioncodeid=r.id).annotate(totalload=Sum('totalloadvalue')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'datetime', 'totalloadvalue')
          l3 = [{**u, **v} for u, v in zip(l1, l2)]       
        for d in l3:
            self.stdout.write(str(d))
