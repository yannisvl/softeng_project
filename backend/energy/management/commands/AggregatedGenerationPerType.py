from django.core.management.base import BaseCommand, CommandError
from energy.models import *
from django.db.models import Sum

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--area', type=str)
        parser.add_argument('--timeres', type=str)
        parser.add_argument('--productiontype', type=str)
        parser.add_argument('--date',  type=str)
        parser.add_argument('--month', type=str)
        parser.add_argument('--year', type=str)

    def handle(self, *args, **options):
        area = options['area']
        timeres = options['timeres']
        r = Resolutioncode.objects.get(resolutioncodetext=timeres)
        prod_type = options['productiontype']
        if prod_type=='AllTypes':
                    if options['date']:
                      date = options['date']
                      s = date.split('-')
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), day=int(s[2]), resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'actualgenerationoutput', 'updatetime', 'mapcodeid', 'productiontypeid')
                    elif options['month']:
                      month=options['month']
                      s = month.split('-')
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), resolutioncodeid=r.id).\
    values('areaname','mapcodeid','areatypecodeid','year','month','day','productiontypeid','resolutioncodeid').order_by('day').\
    annotate(actualgen=Sum('actualgenerationoutput'))
                    elif options['year']:
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(options['year']), resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','productiontypeid','resolutioncodeid').order_by('month').annotate(actualgen=Sum('actualgenerationoutput'))
        else:
                p = Productiontype.objects.get(productiontypetext=prod_type)
                if options['date']:
                      date = options['date']
                      s = date.split('-')
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), day=int(s[2]), productiontypeid=p.id, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'actualgenerationoutput', 'updatetime', 'mapcodeid', 'productiontypeid')
                elif options['month']:
                      month=options['month']
                      s = month.split('-')
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(s[0]), month=int(s[1]), productiontypeid=p.id, resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','day','productiontypeid','resolutioncodeid').order_by('day').annotate(actualgen=Sum('actualgenerationoutput'))
                elif options['year']:
                      l = Aggregatedgenerationpertype.objects.filter(areaname=area, year=int(options['year']), productiontypeid=p.id, resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','productiontypeid','resolutioncodeid').order_by('month').annotate(actualgen=Sum('actualgenerationoutput'))         
        for d in l:
            self.stdout.write(str(d))
