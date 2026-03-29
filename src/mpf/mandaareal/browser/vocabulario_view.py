from Products.Five.browser import BrowserView
from plone import api

class VocabularioView(BrowserView):

    def vocabularios(self):
        brains = api.content.find(
            path={'query': '/mandaareal/vocabulario', 'depth': -1},
            portal_type='Document',
            review_state='published',
            sort_on='title_or_id'
        )

        resultado = []
        for i, brain in enumerate(brains, start=1):
            obj = brain.getObject()

            texto = ''
            if hasattr(obj, 'text') and obj.text:
                texto = obj.text.output  # corpo renderizado (HTML)

            data_formatada = brain.effective.strftime('%d/%m/%y')
            resultado.append({
                'contador': f"{i:02}",
                'id': brain.id,
                'title': brain.Title,
                'description': brain.Description,
                'date': data_formatada,
                'text': texto,
            })

        return resultado
