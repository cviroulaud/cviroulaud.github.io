typedef struct Element Element;
struct Element {
  int nb;
  Element *suivant;
};

typedef struct Liste Liste;
struct Liste {
  Element* premier;
  Element* dernier; // pour file
};