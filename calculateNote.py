class calculateNote:
    def __init__(self):
        self.nota = float(input("Ingrese nota del alumno de 1 a 10: "))

    def calculateGrade(self):
        if self.nota >= 9.1 and self.nota <= 10:
            print("A excelente")
        elif self.nota >= 8.1 and self.nota <= 9:
            print("B muy bien")
        elif self.nota >= 7.5 and self.nota <= 8.0:
            print("C muy bien")
        elif self.nota < 7.5:
            print("R reprobado")
        else:
            print("Nota fuera de rango")
