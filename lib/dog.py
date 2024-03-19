from models import Dog

def create_table(base):
    pass

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    query = session.query(Dog)
    all_dogs = query.all()
    return all_dogs

def find_by_name(session, name):
    pass
    dog = session.query(Dog).filter(Dog.name.like(f'%{name}%')).first()

    return dog



def find_by_id(session, id):
    pass
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    pass

    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session, dog, breed):
    pass
    dog.breed = breed

    session.commit()