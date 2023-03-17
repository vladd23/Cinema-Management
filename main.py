from Domain.cardClientValidator import CardClientValidator
from Domain.filmValidator import FilmValidator
from Repository.repositoryJSON import RepositoryJSON

from Service.cardClientService import CardClientService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from Tests.tests import runAllTests
from UI.consola import Consola


def main():
    runAllTests()
    undoRedoService = UndoRedoService()
    rezervare_repository_json = RepositoryJSON("rezervari.json")

    film_repository_json = RepositoryJSON("filme.json")
    film_validator = FilmValidator()
    film_service = FilmService(film_repository_json, film_validator,
                               rezervare_repository_json,
                               undoRedoService)

    card_repository_json = RepositoryJSON('carduri.json')
    card_validator = CardClientValidator()
    card_service = CardClientService(card_repository_json,
                                     rezervare_repository_json, card_validator,
                                     undoRedoService)

    rezervare_service = RezervareService(rezervare_repository_json,
                                         film_service, card_service,
                                         undoRedoService)

    consola = Consola(film_service, card_service, rezervare_service,
                      undoRedoService)

    consola.run_menu()


if __name__ == '__main__':
    main()
