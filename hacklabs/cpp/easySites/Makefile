
#Variables
APPNAME="hello"
GTKMM_COMPILE=`pkg-config gtkmm-2.4 --cflags`
GTKMM_LINK=`pkg-config gtkmm-2.4 --libs`



$(APPNAME): hello.o ventana.o
	g++ -o hello hello.o ventana.o -lstdc++ $(GTKMM_LINK)

ventana.o: ventana.cpp
	g++ -c ventana.cpp $(GTKMM_COMPILE)

hello.o: hello.cpp
	g++ -c hello.cpp $(GTKMM_COMPILE)
	
clean:
	rm *.o
