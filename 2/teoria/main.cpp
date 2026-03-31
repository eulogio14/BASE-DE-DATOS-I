#include <iostream>
#include <vector>

struct Alumno {
    void ingresarNota(int nota);
    std::vector <int> notas;
};
void Alumno::ingresarNota(int nota) {
    notas.push_back(nota);
}
ostream &print(ostream& os, const Alumno& item) {
    float promedio = 0;
    for (const int nota:item.notas.size())
        promedio += nota;
    promedio = promedio/item.notas|
}