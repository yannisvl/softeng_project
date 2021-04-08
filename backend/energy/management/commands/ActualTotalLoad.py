from django.core.management.base import BaseCommand, CommandError
from energy.models import *
from django.db.models import Sum

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
          l = Actualtotalload.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), day=int(s[2]), resolutioncodeid=r.id).order_by('datetime').values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue', 'updatetime', 'mapcodeid')
        elif options['month']:
          month=options['month']
          s = month.split('-')
          l = Actualtotalload.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), resolutioncodeid=r.id).order_by('datetime').\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day').\
    annotate(totalload=Sum('totalloadvalue'))
        elif options['year']:
          l = Actualtotalload.objects.filter(areaname=area, year=int(options['year']), resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year').\
    order_by('datetime').annotate(totalload=Sum('totalloadvalue'))        
        for d in l:
            self.stdout.write(str(d))
