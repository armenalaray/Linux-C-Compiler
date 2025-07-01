struct Address {
    char city[20];
    char street[50];
};

struct Student {
    int id;
    char name[50];
    struct Address address; // Nested structure
};

struct Student a;

struct Student main(struct Address b, struct Address ale[2])
{
    struct Student student;
    
    //student1.id = 1;
    //strcpy(student1.name, "John Doe");
    //strcpy(student1.address.city, "New York");
    //strcpy(student1.address.street, "Broadway");

    //return 0;
}