from framefox.core.controller.abstract_controller import AbstractController
from framefox.core.routing.decorator.route import Route


class HomeController(AbstractController):
    @Route("/", "index", methods=["GET"])
    async def index(self):
        return self.render("base.html")

    @Route("/home", "home.index", methods=["GET"])
    async def show_home(self):
        return self.render(
            "home/index.html",
            {
                "title": "NotionLike - Votre espace de travail personnel",
                "description": "Organisez vos idées, notes et projets comme dans Notion",
            },
        )

    @Route("/test-editor", "home.test_editor", methods=["GET"])
    async def test_editor(self):
        """Route de redirection vers l'éditeur de test"""
        return self.redirect("/editor")
