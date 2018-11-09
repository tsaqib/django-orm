from data_backend.models import Subscriber


def main():
    sub = Subscriber(name="First Last", email="first.last@email.com")
    sub.save()


if __name__ == '__main__':
    main()
