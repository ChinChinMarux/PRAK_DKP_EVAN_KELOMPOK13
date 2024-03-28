#include <iostream>
#include <string>
#include <fstream>
#include <vector>
//nagasaki
using namespace std;

struct Task
{
    string deskripsi;
    bool selesai;
    Task(const string &desc, bool status = false) : deskripsi(desc), selesai(status) {}
};

class TaskManager
{
private:
    vector<Task> tugas;

public:
    TaskManager()
    {
        tugas = loadTasks();
    }

    vector<Task> loadTasks()
    {
        vector<Task> loadTugas;
        ifstream file("tugas.txt");
    }
};
