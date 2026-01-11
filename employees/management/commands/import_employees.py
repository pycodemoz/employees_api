import csv
from datetime import datetime
from django.core.management import BaseCommand
from employees.models import Employee, Unit


class Command(BaseCommand):
  
  def add_arguments(self, parser):
    parser.add_argument(
      'file_name',
      type=str,
      help='Lista de funcionários em CSV'
    )
    
  def handle(self, *args, **options):
    file_name = options['file_name']
    
    success_count = 0
    error_count = 0
    missing_units = set()
    
    with open(file_name, 'r', encoding='utf-8-sig') as file:
      reader = csv.DictReader(file)
      
      for line_num, row in enumerate(reader, start=2):
        try:
          name = row['name'].strip()
          birthday = datetime.strptime(row['birthday'].strip(), '%Y-%m-%d').date()
          gender = row['gender'].strip()
          academic_level = row['academic_level'].strip()
          course = row['course'].strip()
          id_number = row['id_number'].strip()
          tax_number = row['tax_number'].strip()
          employee_category = row['employee_category'].strip()
          entry_date = datetime.strptime(row['entry_date'].strip(), '%Y-%m-%d').date()
          place_of_work_name = row['place_of_work'].strip()
          
          # Buscar a Unit pelo nome
          try:
            place_of_work = Unit.objects.get(name=place_of_work_name)
          except Unit.DoesNotExist:
            missing_units.add(place_of_work_name)
            self.stdout.write(
              self.style.WARNING(
                f'Linha {line_num}: Unidade "{place_of_work_name}" não encontrada - {name}'
              )
            )
            continue
          
          # Validação básica
          if entry_date < birthday:
            self.stdout.write(
              self.style.WARNING(
                f'Linha {line_num}: Data de entrada ({entry_date}) anterior ao nascimento ({birthday}) - {name}'
              )
            )
          
          Employee.objects.create(
            name=name,
            birthday=birthday,
            gender=gender,
            academic_level=academic_level,
            course=course,
            id_number=id_number,
            tax_number=tax_number,
            employee_category=employee_category,
            entry_date=entry_date,
            place_of_work=place_of_work
          )
          
          self.stdout.write(self.style.SUCCESS(f'✓ {name}'))
          success_count += 1
          
        except Exception as e:
          error_count += 1
          self.stdout.write(
            self.style.ERROR(f'✗ Linha {line_num}: Erro ao processar - {str(e)}')
          )
          
    self.stdout.write('')
    self.stdout.write(self.style.SUCCESS(f'IMPORTAÇÃO CONCLUÍDA!'))
    self.stdout.write(self.style.SUCCESS(f'Sucesso: {success_count} funcionários'))
    
    if error_count > 0:
      self.stdout.write(self.style.ERROR(f'Erros: {error_count} registros'))
    
    if missing_units:
      self.stdout.write('')
      self.stdout.write(self.style.WARNING('Unidades não encontradas no banco:'))
      for unit in sorted(missing_units):
        self.stdout.write(self.style.WARNING(f'  - {unit}'))
      self.stdout.write('')
      self.stdout.write(self.style.NOTICE('Crie essas unidades primeiro com:'))
      for unit in sorted(missing_units):
        self.stdout.write(f'  Unit.objects.create(name="{unit}")')