# fizzbuz.py
class FizzBuzz:
  def get_list(self):
    return range(1, 101)
  
  def check_divisors(self,number):
      if number % 3 == 0 and number % 5 == 0:
          return 'FizzBuzz'
      
      if number % 3 == 0 or '3' in str(number):
          return 'Fizz'
      
      if number % 5 == 0 or '5' in str(number):
          return 'Buzz'
      
      return str(number)

  if __name__ == "__main__":
      # Este código se ejecutará solo si este script es el programa principal
      for i in range(1,31):
          print(check_divisors(i),end=' ')
        
        
        