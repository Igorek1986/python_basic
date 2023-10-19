# Python Basic (Skillbox)

<details>
<summary>Модуль 14</summary>
- [x] Задача 1. Информация о системе  
  - 1. Информация о системе.
      Чтобы преподавателям было проще помогать вам при возникновении различных ошибок, нужно собрать информацию об операционной системе и версии Python. Для этого используйте код ниже.
    ```python
      import platform
      import sys
      info = 'OS info is \n{}\n\nPython version is {} {}'.format(
          platform.uname(),
          sys.version,
          platform.architecture(),
      )
      print(info)  
      with open('os_info.txt', 'w', encoding='utf8') as file:
          file.write(info)
    ```
</details>

