import customtkinter as ctk

TITULO = "Reino das Marés"
COR_FUNDO = "#101923"
COR_PAINEL = "#1b2b38"
COR_DESTAQUE = "#c69b5d"
COR_TEXTO = "#e8e1d5"
COR_SECUNDARIA = "#8fa7b5"

DIALOGOS = {
    "taverna": {
        "titulo": "A Taverna do Farol Partido",
        "texto": (
            "Skanör, ao cair da noite.\n\n"
            "A chuva bate nas janelas de uma taverna antiga. Você é apenas um "
            "pescador, acostumado ao cheiro de sal, às redes molhadas e aos "
            "dias em que o mar não oferece nada.\n\n"
            "Perto da lareira, um senhor de barba branca observa o fogo. "
            "Quando percebe seu olhar, ele começa a falar sobre o Reino das Marés."
        ),
        "perguntar": (
            "Você se aproxima e pergunta: “O que é esse Reino das Marés? "
            "E por que fala dele como se fosse real?”\n\n"
            "O velho responde que existe um território além das águas conhecidas, "
            "onde um dragão guarda algo que os homens jamais deveriam encontrar. "
            "Ele diz que a entrada só aparece quando a maré recua sob uma lua escura."
        ),
        "ouvir": (
            "Você permanece em silêncio, perto da lareira.\n\n"
            "O velho conta que, há muitas gerações, guerreiros partiram em busca "
            "do Reino das Marés. Nenhum voltou. Alguns diziam que um dragão vivia "
            "além do horizonte; outros acreditavam que o próprio mar engolia "
            "qualquer um que tentasse atravessá-lo."
        ),
        "proxima": "pergaminho",
    },
    "pergaminho": {
        "titulo": "A lenda dos que não voltaram",
        "texto": (
            "O senhor retira de dentro do casaco um pedaço de pergaminho "
            "manchado de sal. Há um desenho tosco de uma ilha cercada por "
            "ondas e uma frase quase apagada: “Quando o mar respirar para trás, "
            "a passagem despertará”."
        ),
        "perguntar": (
            "Você pergunta por que nenhum guerreiro retornou.\n\n"
            "O velho aperta os olhos. “Essa é a parte que ninguém conhece. "
            "Não sabemos se foram mortos pelo dragão, se encontraram algo pior "
            "ou se decidiram nunca mais voltar. A lenda não conta o destino deles.”"
        ),
        "ouvir": (
            "Você deixa o velho continuar.\n\n"
            "Ele explica que os relatos mais antigos mencionam três sinais: "
            "um farol apagado, um navio preso entre as pedras e uma maré que "
            "corre na direção contrária. “Se quer encontrar a passagem, "
            "comece procurando esses sinais.”"
        ),
        "proxima": "convite",
    },
    "convite": {
        "titulo": "Um chamado para o desconhecido",
        "texto": (
            "A taverna fica em silêncio por um instante. O velho coloca o "
            "pergaminho sobre a mesa e encara suas mãos calejadas de pescador.\n\n"
            "“Não há exército para enviar desta vez. Talvez seja justamente "
            "por isso que você consiga chegar onde os outros falharam.”"
        ),
        "perguntar": (
            "Você pergunta o que poderia fazer contra um dragão.\n\n"
            "“Não precisa começar como guerreiro”, ele diz. “Precisa descobrir "
            "o caminho, entender o mar e aprender por que os outros desapareceram. "
            "Uma boa decisão pode valer mais que uma espada.”"
        ),
        "ouvir": (
            "Você escuta o estalar da lenha e o som distante das ondas.\n\n"
            "O velho deixa o pergaminho com você. “O mar não escolhe os mais "
            "fortes. Escolhe aqueles que continuam navegando mesmo quando "
            "não entendem as águas.”"
        ),
        "proxima": None,
    },
}

LOCAIS = {
    "Taverna de Skanör": {
        "descricao": "O abrigo dos marinheiros. O velho ainda está junto à lareira.",
        "acoes": ["Conversar com o velho", "Organizar a mochila", "Partir para a costa"],
        "destinos": ["Conversar com o velho", "Organizar a mochila", "Costa de Skanör"],
    },
    "Costa de Skanör": {
        "descricao": "O vento sopra forte. Barcos balançam no cais e gaivotas gritam sobre as pedras.",
        "acoes": ["Examinar as marcas na areia", "Falar com uma pescadora", "Ir ao farol"],
        "destinos": ["Examinar as marcas na areia", "Falar com uma pescadora", "Farol Apagado"],
    },
    "Farol Apagado": {
        "descricao": "A torre está abandonada. A lanterna foi destruída, mas há inscrições na parede.",
        "acoes": ["Ler as inscrições", "Subir até a lanterna", "Seguir para o naufrágio"],
        "destinos": ["Ler as inscrições", "Subir até a lanterna", "Navio Naufragado"],
    },
    "Navio Naufragado": {
        "descricao": "Um navio antigo repousa entre rochedos. A madeira range com o movimento das ondas.",
        "acoes": ["Explorar o convés", "Investigar a cabine", "Preparar a travessia"],
        "destinos": ["Explorar o convés", "Investigar a cabine", "Travessia para o Reino"],
    },
    "Travessia para o Reino": {
        "descricao": "A maré recua de maneira impossível. Um caminho de pedras surge no meio do oceano.",
        "acoes": ["Atravessar o caminho", "Observar o mar antes de seguir"],
        "destinos": ["Reino das Marés", "Observar o mar antes de seguir"],
    },
    "Reino das Marés": {
        "descricao": "O céu é verde-azulado e ondas flutuam no ar como enormes serpentes.",
        "acoes": ["Avançar até o templo", "Observar as ruínas"],
        "destinos": ["Covil do Dragão", "Observar as ruínas"],
    },
    "Covil do Dragão": {
        "descricao": "No coração do reino, uma criatura colossal abre os olhos. A lenda era verdadeira.",
        "acoes": ["Enfrentar o dragão", "Tentar compreender a criatura"],
        "destinos": ["Final: confronto", "Final: diálogo"],
    },
}

TEXTOS_ACOES = {
    "Conversar com o velho": (
        "O velho repete que ninguém sabe o que aconteceu com os guerreiros. "
        "Ele recomenda procurar os sinais deixados na costa."
    ),
    "Organizar a mochila": (
        "Você separa uma corda, uma faca de pesca e um pequeno cantil. "
        "Não é muito, mas é o que tem."
    ),
    "Examinar as marcas na areia": (
        "Você encontra pegadas antigas que terminam de repente na água. "
        "Entre as pedras há uma escama azulada. Uma pista foi adicionada ao diário."
    ),
    "Falar com uma pescadora": (
        "A pescadora conta que viu uma luz sob as ondas na noite passada. "
        "Ela diz que o farol costumava orientar embarcações até mesmo durante tempestades."
    ),
    "Ler as inscrições": (
        "As inscrições dizem: “A passagem não se abre pela força, mas pelo ritmo das marés”. "
        "Você registra a frase no diário."
    ),
    "Subir até a lanterna": (
        "No alto, você encontra um mecanismo enferrujado e um mapa apontando para um navio "
        "preso entre os rochedos."
    ),
    "Explorar o convés": (
        "No convés há marcas de garras enormes. O navio não foi destruído por uma tempestade."
    ),
    "Investigar a cabine": (
        "Você encontra o diário de um guerreiro. A última página diz: "
        "“O dragão não permite que ninguém saia... ou talvez esteja tentando nos proteger”."
    ),
    "Preparar a travessia": (
        "Você amarra a corda à cintura e espera a maré recuar. O caminho para o reino começa a surgir."
    ),
    "Observar o mar antes de seguir": (
        "As ondas se movem para trás. Por um breve instante, você vê silhuetas sob a água, "
        "como pessoas caminhando no fundo do oceano."
    ),
    "Observar as ruínas": (
        "As ruínas exibem nomes gravados em pedra: os guerreiros desaparecidos chegaram até aqui. "
        "O que aconteceu depois continua sendo um mistério."
    ),
}


class ReinoDasMaresApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title(TITULO)
        self.geometry("1050x720")
        self.minsize(850, 620)
        self.configure(fg_color=COR_FUNDO)

        self.jogador = {
            "nome": "Pescador",
            "local": "Taverna de Skanör",
            "pistas": [],
            "inventario": ["Faca de pesca", "Corda", "Cantil"],
            "dialogo_atual": "taverna",
            "etapa_dialogo": 0,
            "perguntou": 0,
            "ouviu": 0,
            "historia_iniciada": False,
            "final": None,
        }

        self._montar_interface()
        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        self.tela_inicial = ctk.CTkFrame(
            self,
            fg_color=COR_FUNDO,
            corner_radius=0
        )
        self.tela_inicial.grid(
            row=0, column=0, rowspan=2, sticky="nsew"
        )

        self.tela_inicial.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.tela_inicial,
            text="⚓",
            font=ctk.CTkFont(size=70),
            text_color=COR_DESTAQUE
        ).pack(pady=(100, 15))

        ctk.CTkLabel(
            self.tela_inicial,
            text="REINO DAS MARÉS",
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=COR_DESTAQUE
        ).pack(pady=10)

        ctk.CTkLabel(
            self.tela_inicial,
            text="Uma lenda esquecida sob as águas",
            font=ctk.CTkFont(size=17),
            text_color=COR_SECUNDARIA
        ).pack(pady=(0, 50))

        ctk.CTkButton(
            self.tela_inicial,
            text="INICIAR AVENTURA",
            width=280,
            height=55,
            fg_color=COR_DESTAQUE,
            hover_color="#a77d45",
            text_color=COR_FUNDO,
            font=ctk.CTkFont(size=17, weight="bold"),
            command=self.iniciar_jogo
        ).pack(pady=12)

        ctk.CTkButton(
            self.tela_inicial,
            text="SAIR",
            width=280,
            height=45,
            fg_color="#35566a",
            hover_color="#52768a",
            command=self.destroy
        ).pack(pady=8)

    def iniciar_jogo(self):
        self.tela_inicial.destroy()
        self.mostrar_abertura()    

    def _montar_interface(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        topo = ctk.CTkFrame(self, fg_color=COR_PAINEL, corner_radius=0, height=76)
        topo.grid(row=0, column=0, sticky="ew")
        topo.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            topo, text="⚓  REINO DAS MARÉS",
            font=ctk.CTkFont(size=27, weight="bold"),
            text_color=COR_DESTAQUE
        ).grid(row=0, column=0, padx=25, pady=(15, 0), sticky="w")

        ctk.CTkLabel(
            topo, text="Uma lenda esquecida sob as águas",
            font=ctk.CTkFont(size=13), text_color=COR_SECUNDARIA
        ).grid(row=1, column=0, padx=28, pady=(0, 12), sticky="w")

        corpo = ctk.CTkFrame(self, fg_color="transparent")
        corpo.grid(row=1, column=0, sticky="nsew", padx=18, pady=18)
        corpo.grid_columnconfigure(0, weight=3)
        corpo.grid_columnconfigure(1, weight=1)
        corpo.grid_rowconfigure(0, weight=1)

        self.painel_historia = ctk.CTkFrame(
            corpo, fg_color=COR_PAINEL, corner_radius=14
        )
        self.painel_historia.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.painel_historia.grid_columnconfigure(0, weight=1)
        self.painel_historia.grid_rowconfigure(1, weight=1)

        self.lbl_titulo_cena = ctk.CTkLabel(
            self.painel_historia, text="",
            font=ctk.CTkFont(size=23, weight="bold"),
            text_color=COR_DESTAQUE, wraplength=650
        )
        self.lbl_titulo_cena.grid(row=0, column=0, padx=25, pady=(24, 12), sticky="w")

        self.texto_historia = ctk.CTkTextbox(
            self.painel_historia, wrap="word",
            font=ctk.CTkFont(size=16), fg_color="#14212b",
            text_color=COR_TEXTO, border_width=0
        )
        self.texto_historia.grid(row=1, column=0, padx=22, pady=10, sticky="nsew")

        self.frame_escolhas = ctk.CTkFrame(
            self.painel_historia, fg_color="transparent"
        )
        self.frame_escolhas.grid(row=2, column=0, padx=20, pady=(8, 22), sticky="ew")
        self.frame_escolhas.grid_columnconfigure((0, 1), weight=1)

        painel_lateral = ctk.CTkFrame(
            corpo, fg_color=COR_PAINEL, corner_radius=14, width=250
        )
        painel_lateral.grid(row=0, column=1, sticky="nsew")
        painel_lateral.grid_propagate(False)

        ctk.CTkLabel(
            painel_lateral, text="DIÁRIO DE BORDO",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=COR_DESTAQUE
        ).pack(padx=15, pady=(22, 14))

        self.lbl_local = ctk.CTkLabel(
            painel_lateral, text="", font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COR_TEXTO, wraplength=210
        )
        self.lbl_local.pack(padx=15, pady=5)

        self.lbl_pistas = ctk.CTkLabel(
            painel_lateral, text="", justify="left",
            text_color=COR_SECUNDARIA, wraplength=210
        )
        self.lbl_pistas.pack(padx=15, pady=(15, 8), anchor="w")

        self.lbl_mochila = ctk.CTkLabel(
            painel_lateral, text="", justify="left",
            text_color=COR_SECUNDARIA, wraplength=210
        )
        self.lbl_mochila.pack(padx=15, pady=8, anchor="w")

        self.lbl_escolhas = ctk.CTkLabel(
            painel_lateral, text="", justify="left",
            text_color=COR_SECUNDARIA, wraplength=210
        )
        self.lbl_escolhas.pack(padx=15, pady=8, anchor="w")

        self.btn_recomecar = ctk.CTkButton(
            painel_lateral, text="Recomeçar história",
            fg_color="#435765", hover_color="#526d7d",
            command=self.recomecar
        )
        self.btn_recomecar.pack(side="bottom", padx=15, pady=18, fill="x")

    def escrever_historia(self, texto):
        self.texto_historia.configure(state="normal")
        self.texto_historia.delete("1.0", "end")
        self.texto_historia.insert("end", texto)
        self.texto_historia.configure(state="disabled")

    def limpar_escolhas(self):
        for widget in self.frame_escolhas.winfo_children():
            widget.destroy()

    def criar_botao(self, texto, comando, coluna, cor="#35566a"):
        botao = ctk.CTkButton(
            self.frame_escolhas,
            text=texto,
            command=comando,
            height=48,
            corner_radius=9,
            fg_color=cor,
            hover_color="#52768a",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        botao.grid(row=0, column=coluna, padx=7, pady=6, sticky="ew")
        return botao

    def atualizar_diario(self):
        self.lbl_local.configure(text=f"LOCAL\n{self.jogador['local']}")

        pistas = self.jogador["pistas"]
        if pistas:
            texto_pistas = "PISTAS\n" + "\n".join(f"• {pista}" for pista in pistas)
        else:
            texto_pistas = "PISTAS\nNenhuma pista encontrada."
        self.lbl_pistas.configure(text=texto_pistas)

        itens = self.jogador["inventario"]
        texto_itens = "MOCHILA\n" + "\n".join(f"• {item}" for item in itens)
        self.lbl_mochila.configure(text=texto_itens)

        self.lbl_escolhas.configure(
            text=(
                "SUAS ESCOLHAS\n"
                f"Perguntou: {self.jogador['perguntou']}\n"
                f"Ouviu: {self.jogador['ouviu']}"
            )
        )

    def adicionar_pista(self, pista):
        if pista not in self.jogador["pistas"]:
            self.jogador["pistas"].append(pista)
        self.atualizar_diario()

    def mostrar_abertura(self):
        self.jogador["local"] = "Taverna de Skanör"
        self.lbl_titulo_cena.configure(text="A Taverna do Farol Partido")
        texto = (
            "SKANÖR — NOITE CHUVOSA\n\n"
            "Você é um mero pescador. Sua vida sempre foi simples: lançar as redes, "
            "esperar a maré e voltar para casa antes que a tempestade chegasse.\n\n"
            "Nesta noite, porém, um senhor misterioso sentado junto à lareira "
            "começa a contar uma lenda sobre o Reino das Marés — um lugar além "
            "do oceano, onde um dragão repousa.\n\n"
            "Dizem que muitos guerreiros partiram para enfrentá-lo. Nenhum voltou. "
            "Ninguém sabe o motivo.\n\n"
            "O velho percebe que você está ouvindo e faz um gesto para que se aproxime.\n\n"
            "Como você reage?"
        )
        self.escrever_historia(texto)
        self.limpar_escolhas()
        self.criar_botao("Perguntar sobre a lenda", self.iniciar_dialogo_perguntar, 0)
        self.criar_botao("Ouvir em silêncio", self.iniciar_dialogo_ouvir, 1)
        self.atualizar_diario()

    def iniciar_dialogo_perguntar(self):
        self.jogador["perguntou"] += 1
        self.mostrar_resposta_dialogo("perguntar")

    def iniciar_dialogo_ouvir(self):
        self.jogador["ouviu"] += 1
        self.mostrar_resposta_dialogo("ouvir")

    def mostrar_resposta_dialogo(self, escolha):
        cena = DIALOGOS[self.jogador["dialogo_atual"]]
        resposta = cena[escolha]

        if self.jogador["dialogo_atual"] == "taverna":
            self.adicionar_pista("Existe um Reino das Marés além do oceano.")
        elif self.jogador["dialogo_atual"] == "pergaminho":
            if escolha == "perguntar":
                self.adicionar_pista("O destino dos guerreiros desaparecidos é desconhecido.")
            else:
                self.adicionar_pista("Três sinais: farol apagado, navio naufragado e maré invertida.")

        self.lbl_titulo_cena.configure(text=cena["titulo"])
        self.escrever_historia(cena["texto"] + "\n\n" + resposta)
        self.limpar_escolhas()

        proxima = cena["proxima"]
        if proxima is None:
            self.criar_botao("⚓ Começar exploração", self.iniciar_exploracao, 0)
            self.criar_botao("📜 Rever a lenda", self.mostrar_abertura, 1)
        else:
            self.criar_botao(
                "Fazer outra pergunta",
                lambda: self.avancar_dialogo("perguntar", proxima), 0
            )
            self.criar_botao(
                "Continuar ouvindo",
                lambda: self.avancar_dialogo("ouvir", proxima), 1
            )
        self.atualizar_diario()

    def avancar_dialogo(self, escolha, proxima):
        self.jogador["dialogo_atual"] = proxima
        if escolha == "perguntar":
            self.jogador["perguntou"] += 1
        else:
            self.jogador["ouviu"] += 1
        self.mostrar_resposta_dialogo(escolha)

    def iniciar_exploracao(self):
        self.jogador["historia_iniciada"] = True
        self.jogador["local"] = "Taverna de Skanör"
        self.mostrar_local()

    def mostrar_local(self):
        local = self.jogador["local"]
        dados = LOCAIS[local]

        self.lbl_titulo_cena.configure(text=local)
        self.escrever_historia(
            f"{local.upper()}\n\n{dados['descricao']}\n\n"
            "O que você deseja fazer?"
        )
        self.limpar_escolhas()

        acoes = dados["acoes"]
        for indice, acao in enumerate(acoes):
            coluna = indice % 2
            linha = indice // 2
            botao = ctk.CTkButton(
                self.frame_escolhas,
                text=acao,
                command=lambda escolha=acao: self.executar_acao(escolha),
                height=45,
                fg_color="#35566a",
                hover_color="#52768a"
            )
            botao.grid(row=linha, column=coluna, padx=7, pady=6, sticky="ew")

        self.frame_escolhas.grid_columnconfigure((0, 1), weight=1)
        self.atualizar_diario()

    def executar_acao(self, acao):
        local = self.jogador["local"]

        if acao == "Partir para a costa":
            self.mover_para("Costa de Skanör")
            return
        elif acao == "Ir ao farol":
            self.mover_para("Farol Apagado")
            return
        elif acao == "Seguir para o naufrágio":
            self.mover_para("Navio Naufragado")
            return
        elif acao == "Preparar a travessia":
            self.mover_para("Travessia para o Reino")
            return
        elif acao == "Atravessar o caminho":
            self.mover_para("Reino das Marés")
            return
        elif acao == "Avançar até o templo":
            self.mover_para("Covil do Dragão")
            return
        elif acao == "Enfrentar o dragão":
            self.mostrar_final("confronto")
            return
        elif acao == "Tentar compreender a criatura":
            self.mostrar_final("dialogo")
            return

        resultado = TEXTOS_ACOES.get(acao, "Você observa o lugar com atenção.")
        if acao == "Examinar as marcas na areia":
            self.adicionar_pista("Uma escama azulada encontrada na costa.")
        elif acao == "Ler as inscrições":
            self.adicionar_pista("A passagem se abre pelo ritmo das marés.")
        elif acao == "Investigar a cabine":
            self.adicionar_pista("O diário sugere que o dragão pode estar protegendo algo.")
        elif acao == "Explorar o convés":
            self.adicionar_pista("O navio foi atacado por uma criatura com garras enormes.")
        elif acao == "Subir até a lanterna":
            self.adicionar_pista("O mapa do farol aponta para o navio naufragado.")

        self.lbl_titulo_cena.configure(text=acao)
        self.escrever_historia(resultado + "\n\nO que fará agora?")
        self.limpar_escolhas()
        self.criar_botao("Continuar explorando", self.mostrar_local, 0)
        self.criar_botao("Consultar o diário", self.mostrar_diario, 1)

    def mover_para(self, destino):
        if destino == "Travessia para o Reino" and len(self.jogador["pistas"]) == 0:
            self.escrever_historia(
                "A maré ainda não recuou. Você sente que falta compreender "
                "alguma coisa sobre a lenda antes de tentar a travessia."
            )
            self.limpar_escolhas()
            self.criar_botao("Voltar", self.mostrar_local, 0)
            return

        self.jogador["local"] = destino
        self.mostrar_local()

    def mostrar_diario(self):
        texto = (
            "DIÁRIO DE BORDO\n\n"
            "Pistas encontradas:\n"
            + ("\n".join(f"• {p}" for p in self.jogador["pistas"])
               if self.jogador["pistas"] else "Nenhuma pista.")
            + "\n\nVocê ainda não sabe por que os guerreiros nunca retornaram."
        )
        self.lbl_titulo_cena.configure(text="Diário de bordo")
        self.escrever_historia(texto)
        self.limpar_escolhas()
        self.criar_botao("Voltar à exploração", self.mostrar_local, 0)

    def mostrar_final(self, tipo):
        self.jogador["final"] = tipo
        self.lbl_titulo_cena.configure(text="O coração do Reino das Marés")

        if tipo == "confronto":
            texto = (
                "O dragão ergue a cabeça e suas escamas brilham como o fundo do oceano.\n\n"
                "Você segura sua faca de pesca. Não é um guerreiro lendário, nem possui "
                "uma espada encantada. É apenas alguém que atravessou o mar para descobrir "
                "a verdade.\n\n"
                "A criatura ruge, e as águas ao redor do templo se levantam. "
                "Sua história termina no instante em que você dá o primeiro passo "
                "em direção ao dragão.\n\n"
                "FINAL: O DESAFIO DO DRAGÃO"
            )
        else:
            texto = (
                "Você abaixa a faca e observa os olhos antigos da criatura.\n\n"
                "O dragão não ataca. Em sua voz, você escuta o som de correntes "
                "e de ondas distantes. Ele revela que os guerreiros chegaram ao reino, "
                "mas escolheram permanecer para proteger a passagem de algo que vive "
                "nas profundezas.\n\n"
                "Talvez a lenda tenha escondido a verdade: ninguém voltou porque "
                "alguém precisava ficar.\n\n"
                "FINAL: O SEGREDO DAS MARÉS"
            )

        self.escrever_historia(texto)
        self.limpar_escolhas()
        self.criar_botao("Recomeçar aventura", self.recomecar, 0)
        self.criar_botao("Fechar jogo", self.destroy, 1)

    def recomecar(self):
        self.jogador = {
            "nome": "Pescador",
            "local": "Taverna de Skanör",
            "pistas": [],
            "inventario": ["Faca de pesca", "Corda", "Cantil"],
            "dialogo_atual": "taverna",
            "etapa_dialogo": 0,
            "perguntou": 0,
            "ouviu": 0,
            "historia_iniciada": False,
            "final": None,
        }
        self.mostrar_abertura()

if __name__ == "__main__":
    app = ReinoDasMaresApp()
    app.mainloop()
