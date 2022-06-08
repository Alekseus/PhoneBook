import record_tel
import search_tel
import user_interface
import logger

def run():
     temp = user_interface.choice()
     if temp == 1:
          print ('Внесение нового контакта')
          entry = record_tel.record()
          logger.log_to_file(entry)
          run()
     if temp == 2:
          print ('\nПоиск контакта\n' )
          entry = search_tel.search()
          logger.reading_file(entry)
          run()
     if temp == 3:
          print ('\nВывод всех контактов справочника\n\
              \n=== КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n')
          logger.read_all_file()
          run()
     if temp == 4:
          print('\n Работа справочника окончена.\n')
          exit
