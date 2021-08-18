import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot('ndmvp',database_uri='mysql://root:root@localhost/chat',read_only=True,)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({'text': 'The attribute "text" is required.' }, status=400)
        # if "'text': ''" in input_data:
        #     print(input_data)
        #     response = {}
        #     print('text black')
        #     response['text']='The attribute "text" is required'
        #     return JsonResponse(response, status=400)
        print('input data',input_data)
        print("")
        # trainer = ChatterBotCorpusTrainer(self.chatterbot)
        # trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations" )
        
        # response = chatbot.get_response('What is your Number')
        # print(response)
  
        # response = chatbot.get_response('Who are you?')
        # print(response)
        response = self.chatterbot.get_response(input_data)
        print("responce",response)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
