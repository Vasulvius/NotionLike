from fastapi.requests import Request
from framefox.core.controller.abstract_controller import AbstractController
from framefox.core.routing.decorator.route import Route


class EditorController(AbstractController):
    """Contrôleur pour l'éditeur de pages NotionLike"""

    @Route("/editor", "editor.show", methods=["GET"])
    async def show_editor(self, request: Request):
        """Affiche la page d'édition"""
        # Données de test pour une page
        test_blocks = [
            {"id": "block_1", "type": "heading_1", "content": {"text": "Mon premier titre"}, "position": 0},
            {
                "id": "block_2",
                "type": "paragraph",
                "content": {"text": "Voici un paragraphe de test. Vous pouvez éditer ce texte."},
                "position": 1,
            },
            {"id": "block_3", "type": "paragraph", "content": {"text": ""}, "position": 2},
        ]

        return self.render("editor/page.html", {"title": "Éditeur NotionLike", "page_title": "Page de test", "blocks": test_blocks})

    @Route("/editor/api/blocks", "editor.api.save_blocks", methods=["POST"])
    async def save_blocks(self, request: Request):
        """API pour sauvegarder les blocs (simulation)"""
        try:
            data = await request.json()
            blocks = data.get("blocks", [])

            # Pour l'instant, on fait juste un log des données reçues
            print(f"📝 Sauvegarde de {len(blocks)} blocs:")
            for block in blocks:
                print(f"  - {block.get('type')}: {block.get('content', {}).get('text', '')[:50]}...")

            return self.json({"success": True, "message": f"{len(blocks)} blocs sauvegardés", "blocks_saved": len(blocks)})

        except Exception as e:
            return self.json({"success": False, "error": str(e)}, status_code=400)
