# Определите класс Filename, который представляет имя файла. Имя файла состоит из
# базового имени и расширения. Например: имя файла 'rapport.docx'
# состоит из базового имени 'rapport' и расширения 'docx' (которое указывает, что это
# документ Word); имя файла 'movie.mp4' состоит из базового имени 'movie' и
# расширения 'mp4' (которое указывает, что это видеоролик в формате MP4).
#
# Класс Filename должен иметь конструктор с двумя параметрами, а именно двумя строками, которые
# представляют базовое имя и расширение имени файла. Предполагается, что обе строки
# не пусты и содержат только буквы.
#
# Также добавьте следующие методы в класс Filename:
# - get_basename: возвращает базовое имя (имя файла без расширения);
#                 этот метод не имеет параметров.
# - get_extension: возвращает расширение имени файла;
#                 этот метод не имеет параметров.
# - get_filename: возвращает полное имя файла. Это базовое имя с точкой
#                 и завершающееся расширением;
#                 этот метод не имеет параметров.
#
# - set_basename: этот метод имеет один параметр и изменяет базовое имя файла на значение параметра;
#                 предполагается, что параметр является непустой строкой, содержащей только буквы.
# - set_extension: этот метод имеет один параметр и изменяет расширение имени файла на значение параметра;
#                 предполагается, что параметр является непустой строкой, содержащей только буквы.
#
# - rename: этот метод имеет один параметр, а именно строку, которая в принципе состоит из
#           букв (базовое имя), за которыми следует точка, за которой следуют еще несколько букв
#           (расширение), и, таким образом, представляет собой полное имя файла;
#           этот метод изменяет базовое имя и расширение объекта на основе параметра.
#           В любом случае параметр содержит только буквы и точки, это можно считать правильным. Однако
#           возможно, что параметр все же 'недействителен':
#           - строка может содержать несколько точек или даже не содержать точек
#           - буквы, представляющие базовое имя, могут образовывать пустую строку
#           - буквы, представляющие расширение, могут образовывать пустую строку
#           В этих случаях этот метод должен вызывать AssertionError (с помощью оператора assert),
#           и базовое имя и расширение объекта не должны изменяться.
#
# - compare: этот метод имеет один параметр, а именно (другой) объект типа Filename; этот
#            метод сравнивает имя файла объекта, на котором этот метод вызывается,
#            с объектом Filename, переданным в качестве параметра;
#            метод возвращает значение True, если имена файлов одинаковы, и False в противном случае.
#
# Основная функция ниже содержит несколько примеров, чтобы проиллюстрировать требуемую функциональность.
#
# Вы не можете добавлять дополнительные операторы импорта в вашу программу.

# >>> Вставьте здесь ваши определения классов <<<

class Filename:
    def __init__(self, basename, extension):
        assert type(basename) == str
        assert type(extension) == str
        assert len(basename) != 0
        assert len(extension) != 0
        self.basename = basename
        self.extension = extension

    def get_basename(self):
        return self.basename

    def get_extension(self):
        return self.extension

    def get_filename(self):
        assert type(basename) == str
        assert type(extension) == str
        return self.basename + '.' + self.extension

    def set_basename(self, basename):
        assert len(basename) != 0
        assert type(basename) == str

        self.basename = basename

    def set_extension(self, extension):
        assert len(extension) != 0
        assert type(extension) == str

        self.extension = extension

    def rename(self, filename):
        assert filename.split('.')
        assert len(basename) != 0
        assert len(extension) != 0

        parts = filename.split('.')
        basename = parts[0]
        extension = parts[1]


    def compare(self, other):
        if self.get_filename() == other.get_filename():
            return True
        return False


######################################################################
                      #
######################################################################
def main():
    file1 = Filename("doc", "pdf")
    assert file1.get_basename() == "doc"
    assert file1.get_extension() == "pdf"
    assert file1.get_filename() == "doc.pdf"

    file1.set_basename("rapport")
    file1.set_extension("docx")
    assert file1.get_basename() == "rapport"
    assert file1.get_extension() == "docx"
    assert file1.get_filename() == "rapport.docx"

    file1.rename("movie.mp4")
    assert file1.get_basename() == "movie"
    assert file1.get_extension() == "mp4"

    try:
        file1.rename("wrong..")
    except AssertionError:
        assert file1.get_basename() == "movie"
        assert file1.get_extension() == "mp4"
    else:
        assert False, "ASSERTIONERROR!!"

    assert file1.get_basename() == "movie"
    assert file1.get_extension() == "mp4"

    file2 = Filename("something", "mp4")
    assert file1.compare(file2) == False

    file2 = Filename("movie", "avi")
    assert file1.compare(file2) == False

    file2 = Filename("movie", "mp4")
    assert file1.compare(file2) == True



if __name__ == "__main__":
    main()

