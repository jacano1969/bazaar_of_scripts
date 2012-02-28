#include "ventana.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

Ventana::Ventana()
{
    std::cout<<"[DEBUG]:Constructor de la ventana"<<std::endl;

    Glib::RefPtr<Gtk::Builder> glade;
    glade=Gtk::Builder::create_from_file("simpleGlade.glade");
    glade->get_widget("window",window);

    Gtk::Button * button;
    glade->get_widget("button",button);
    button->signal_clicked().connect(sigc::mem_fun(*this, &Ventana::on_button_click));

}

Ventana::~Ventana()
{
    for (int n=0;n<mivector.size();n++)
    {
        std::cout<<"[DEBUG] Datos: "<<mivector[n]<<std::endl;
    }
    cout<<"[DEBUG] Botonsito ha sido presionado "<<mivector.size()<<" veces"<<endl;
    std::cout<<"[DEBUG]:Destructor de la ventana"<<std::endl;
}

void Ventana::on_button_click()
{
    mivector.push_back("botonsito presionao");
    std::cout<<"[DEBUG]: Botonsito presionao"<<std::endl;
}
