#include <iostream>
#include <glibmm.h>
#include <gtkmm.h>
#include <vector>
#include <string>

class Ventana
{
	public:

    std::vector<std::string> mivector;
    Gtk::Window * window;

    Ventana();
    ~Ventana();

    private:
    void on_button_click();
};

