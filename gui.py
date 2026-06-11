import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog
import platform

# ── Language Strings ───────────────────────────────────────────────────────────
LANG = {
    "EN": {
        "title":           "Two-Pass Compiler",
        "subtitle":        "Lexical · Syntax · Semantic Analysis",
        "source_code":     "Source Code",
        "load_sample":     "Load Sample",
        "demo_label":      "Demo",
        "demo_input":      "Input + Branch",
        "demo_arithmetic": "Arithmetic",
        "demo_counter":    "Counter Loop",
        "demo_stop":       "STOP Boundary",
        "demo_syntax_error": "Syntax Errors",
        "demo_semantic_error": "Semantic Errors",
        "analyze":         "Analyze",
        "clear":           "Clear",
        "tab_tokens":      "Token Stream",
        "tab_symbols":     "Symbol Table",
        "tab_ast":         "Syntax Tree",
        "tab_errors":      "Errors",
        "tab_guide":       "Guide",
        "col_line":        "Line",
        "col_type":        "Type",
        "col_value":       "Value",
        "col_name":        "Name",
        "col_scope":       "Scope",
        "col_memory":      "Memory",
        "col_stored":      "Stored Value",
        "col_syntax":      "Syntax",
        "col_assembly":    "Assembly",
        "col_desc":        "Description",
        "tips_title":      "Tips",
        "col_command":     "Command",
        "col_usage":       "Usage Tip",
        "no_errors":       "✓  No errors found.",
        "lex_errors":      "LEXICAL ERRORS",
        "syn_errors":      "SYNTAX ERRORS",
        "sem_errors":      "SEMANTIC ERRORS",
        "ready":           "Ready",
        "analyzing":       "Analyzing…",
        "done":            "Analysis complete",
        "lang_btn":        "🌐 Türkçe",
    },
    "TR": {
        "title":           "İki Geçişli Derleyici",
        "subtitle":        "Sözcüksel · Sözdizimsel · Anlamsal Analiz",
        "source_code":     "Kaynak Kod",
        "load_sample":     "Örnek Yükle",
        "demo_label":      "Demo",
        "demo_input":      "Girdi + Kosul",
        "demo_arithmetic": "Aritmetik",
        "demo_counter":    "Sayac Dongusu",
        "demo_stop":       "STOP Siniri",
        "demo_syntax_error": "Syntax Hatalari",
        "demo_semantic_error": "Semantic Hatalari",
        "analyze":         "Analiz Et",
        "clear":           "Temizle",
        "tab_tokens":      "Token Akışı",
        "tab_symbols":     "Sembol Tablosu",
        "tab_ast":         "Sözdizim Ağacı",
        "tab_errors":      "Hatalar",
        "tab_guide":       "Guide",
        "col_line":        "Satır",
        "col_type":        "Tür",
        "col_value":       "Değer",
        "col_name":        "Ad",
        "col_scope":       "Kapsam",
        "col_memory":      "Bellek",
        "col_stored":      "Girilen Deger",
        "col_syntax":      "Yazim",
        "col_assembly":    "Assembly",
        "col_desc":        "Aciklama",
        "tips_title":      "İpuçları",
        "col_command":     "Komut",
        "col_usage":       "Kullanım ipucu",
        "no_errors":       "✓  Hata bulunamadı.",
        "lex_errors":      "SÖZCÜKSEL HATALAR",
        "syn_errors":      "SÖZDİZİMSEL HATALAR",
        "sem_errors":      "ANLAMSAL HATALAR",
        "ready":           "Hazır",
        "analyzing":       "Analiz ediliyor…",
        "done":            "Analiz tamamlandı",
        "lang_btn":        "🌐 English",
    },
}

# ── Palette ────────────────────────────────────────────────────────────────────
C = {
    "bg":          "#F0EEF8",   # lavender mist – main background
    "surface":     "#FAFAFF",   # near-white panels
    "panel":       "#FFFFFF",   # card white
    "sidebar":     "#E8E5F5",   # slightly deeper lavender for left pane
    "accent":      "#7C6FCF",   # soft purple
    "accent2":     "#A89FE0",   # lighter purple
    "accent_fg":   "#FFFFFF",
    "text":        "#2E2B4A",   # deep slate-purple
    "text_soft":   "#7A7899",   # muted label
    "border":      "#D8D4EE",
    "success":     "#5BAD8F",
    "error":       "#C2616A",
    "warning":     "#C29A61",
    "row_even":    "#F5F3FC",
    "row_odd":     "#FFFFFF",
    "header_bg":   "#E0DCF4",
    "status_bg":   "#EAE8F5",
    "editor_bg":   "#FDFCFF",
    "editor_fg":   "#2E2B4A",
    "scrollbar":   "#C8C2E8",
    "btn_hover":   "#6B5EC0",
    "btn2_bg":     "#EAE8F5",
    "btn2_hover":  "#D8D4EE",
}

FONT_FAMILY = "Segoe UI" if platform.system() == "Windows" else "SF Pro Display" if platform.system() == "Darwin" else "Ubuntu"
MONO_FAMILY = "Cascadia Code" if platform.system() == "Windows" else "Menlo" if platform.system() == "Darwin" else "Ubuntu Mono"

# ── Sample Code ────────────────────────────────────────────────────────────────
GUIDE_ROWS = {
    "EN": [
        ("NAT", "ALLOC NAT", "Integer number type"),
        ("COMMA", "ALLOC COMMA", "Decimal number type"),
        ("TWINAT", "ALLOC TWINAT", "Double integer type"),
        ("TWINCO", "ALLOC TWINCO", "Double decimal type"),
        ("RUN 100", "ORG 100", "Starts program at address 100"),
        ("STOP", "RET", "Stops program execution"),
        ("GIVE ->", "OUT TEXT", "Writes text output"),
        ("TAKE <-", "IN x", "Asks user input"),
        ("x BY 10", "MOV x, 10", "Assigns value to variable"),
        ("THIS", "JMP_FALSE", "Runs when true"),
        ("OR", "JMP_ELSE", "Runs otherwise"),
        ("WHEN", "LOOP_WHILE", "Conditional loop"),
        ("CYC", "LOOP_RANGE", "Range counter loop"),
        ("NEXT x", "INC x", "Increases variable"),
        ("EX x", "DEC x", "Decreases variable"),
        ("PLUS", "ADD", "Adds two values"),
        ("MINUS", "SUB", "Subtracts two values"),
        ("BUMP", "MUL", "Multiplies two values"),
        ("CUT", "DIV", "Divides two values"),
    ],
    "TR": [
        ("NAT", "ALLOC NAT", "Tam sayi tipi"),
        ("COMMA", "ALLOC COMMA", "Ondalik sayi tipi"),
        ("TWINAT", "ALLOC TWINAT", "Double tam sayi"),
        ("TWINCO", "ALLOC TWINCO", "Double ondalik tip"),
        ("RUN 100", "ORG 100", "Programi 100. adresten baslatir"),
        ("STOP", "RET", "Programi durdurur"),
        ("GIVE ->", "OUT TEXT", "Ekrana metin yazar"),
        ("TAKE <-", "IN x", "Kullanicidan veri ister"),
        ("x BY 10", "MOV x, 10", "Degiskene deger atar"),
        ("THIS", "JMP_FALSE", "Kosul dogruysa calisir"),
        ("OR", "JMP_ELSE", "Aksi durumda calisir"),
        ("WHEN", "LOOP_WHILE", "Kosullu dongu baslatir"),
        ("CYC", "LOOP_RANGE", "Aralik dongusu baslatir"),
        ("NEXT x", "INC x", "Degiskeni bir artirir"),
        ("EX x", "DEC x", "Degiskeni bir azaltir"),
        ("PLUS", "ADD", "Toplama islemi yapar"),
        ("MINUS", "SUB", "Cikarma islemi yapar"),
        ("BUMP", "MUL", "Carpma islemi yapar"),
        ("CUT", "DIV", "Bolme islemi yapar"),
    ],
}

GUIDE_TIPS = {
    "EN": [
        ("RUN 100;", "Program starts at address 100; keep the semicolon here."),
        ("STOP;", "Program stops here; code after STOP is ignored."),
        ("NAT x", "Declare a variable on its own line; no semicolon is needed."),
        ("x BY 10", "Assign a direct value to an existing variable."),
        ("result [ x PLUS y BUMP 2]", "Bracket expressions are evaluated with BUMP/CUT before PLUS/MINUS."),
        ("EX x", "Decreases x by 1 without writing x BY EX x."),
        ("NEXT x", "Increases x by 1 without writing x BY NEXT x."),
        ("TAKE <-", "Prompt text should mention a declared variable name, such as Enter x."),
        ("GIVE ->", "Writes a string literal or expression result to output."),
    ],
    "TR": [
        ("RUN 100;", "Program 100. adresten baslar; noktalı virgül burada kullanilir."),
        ("STOP;", "Program burada durur; STOP sonrasindaki kod yok sayilir."),
        ("NAT x", "Degiskeni tek satirda tanimla; noktalı virgül gerekmez."),
        ("x BY 10", "Var olan degiskene dogrudan deger atar."),
        ("result [ x PLUS y BUMP 2]", "Koseli parantezde once BUMP/CUT, sonra PLUS/MINUS hesaplanir."),
        ("EX x", "x degerini x BY EX x yazmadan 1 azaltir."),
        ("NEXT x", "x degerini x BY NEXT x yazmadan 1 artirir."),
        ("TAKE <-", "Girdi metni Enter x gibi tanimli bir degisken adini icermelidir."),
        ("GIVE ->", "String ya da ifade sonucunu ciktiya yazar."),
    ],
}

SAMPLE_CODE = """\
RUN 100;

NAT x
NAT y
COMMA result
TWINAT total
TWINCO average

TAKE <- "Enter x"
TAKE <- "Enter y"

result [ x PLUS y BUMP 2]
total [ x PLUS y]
average [ result CUT 2.0]

THIS (result > 15) {
    GIVE -> "Result is large"
} OR {
    GIVE -> "Result is small"
}

WHEN (x > 0) {
    EX x
}

CYC (NAT i = 0, 5, NEXT) {
    GIVE -> "Loop running"
}

STOP;
"""


# ══════════════════════════════════════════════════════════════════════════════
DEMO_KEYS = [
    "demo_input",
    "demo_arithmetic",
    "demo_counter",
    "demo_stop",
    "demo_syntax_error",
    "demo_semantic_error",
]

DEMO_CODES = {
    "demo_input": SAMPLE_CODE,
    "demo_arithmetic": """\
RUN 100;

NAT x
NAT y
COMMA result
TWINCO average

x BY 10
y BY 3

result [ x PLUS y BUMP 2]
average [ result CUT 2.0]

GIVE -> "Arithmetic demo complete"

STOP;
""",
    "demo_counter": """\
RUN 100;

NAT counter
NAT limit
COMMA score

counter BY 0
limit BY 3
score BY 12.5

NEXT counter
NEXT counter
EX limit
score [ score PLUS counter BUMP 2]

WHEN (counter > 0) {
    GIVE -> "Counter is active"
}

CYC (NAT i = 0, 4, NEXT) {
    GIVE -> "Loop tick"
}

STOP;
""",
    "demo_stop": """\
RUN 100;

NAT x
COMMA result

x BY 8
result [ x CUT 2.0]

GIVE -> "Code before STOP is analyzed"

STOP;

unknown BY 99
result BY "ignored after stop"
""",
    "demo_syntax_error": """\
RUN 100;

NAT x
COMMA result

x BY 10
result [ x PLUS ]

THIS (result > 5 {
    GIVE -> "Missing parenthesis"
}

STOP;
""",
    "demo_semantic_error": """\
RUN 100;

NAT x
COMMA result

x BY 3.14
result BY "hello"
total [ x PLUS missingValue]

STOP;
""",
}


class LineNumbers(tk.Canvas):
    """A canvas that draws line numbers in sync with a paired Text widget."""

    def __init__(self, parent, text_widget: tk.Text, **kwargs):
        super().__init__(
            parent,
            bg=C["sidebar"],
            highlightthickness=0,
            bd=0,
            **kwargs,
        )
        self.text_widget = text_widget
        self._font = (MONO_FAMILY, 11)
        self._last_line_count = 0

        # Keep canvas width snug around the widest line number
        self.configure(width=self._calc_width(1))

        # Wire up synchronisation events on the paired text widget
        text_widget.bind("<<Change>>",          self._on_change, add=True)
        text_widget.bind("<Configure>",         self._on_change, add=True)
        text_widget.bind("<KeyRelease>",        self._on_change, add=True)
        text_widget.bind("<MouseWheel>",        self._on_scroll, add=True)
        text_widget.bind("<Button-4>",          self._on_scroll, add=True)
        text_widget.bind("<Button-5>",          self._on_scroll, add=True)
        text_widget.bind("<<Scroll>>",          self._on_scroll, add=True)

    # ── helpers ───────────────────────────────────────────────────────────────
    def _calc_width(self, line_count: int) -> int:
        digits = max(3, len(str(line_count)))
        return digits * 9 + 18          # ~9 px per digit + padding

    def _on_change(self, *_):
        self.after_idle(self.redraw)

    def _on_scroll(self, *_):
        self.after_idle(self.redraw)

    # ── drawing ───────────────────────────────────────────────────────────────
    def redraw(self):
        self.delete("all")

        total_lines = int(self.text_widget.index("end-1c").split(".")[0])
        new_width   = self._calc_width(total_lines)
        if new_width != self.winfo_width():
            self.configure(width=new_width)

        # Separator line on the right edge
        self.create_line(new_width - 1, 0, new_width - 1, self.winfo_height(),
                         fill=C["border"], width=1)

        # current line highlight
        cur_line = int(self.text_widget.index(tk.INSERT).split(".")[0])

        i = "@0,0"
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y          = dline[1]
            linenum    = int(self.text_widget.index(i).split(".")[0])
            is_current = linenum == cur_line

            # subtle highlight pill for the current line
            if is_current:
                self.create_rectangle(4, y - 1, new_width - 6, y + dline[3] + 1,
                                      fill=C["accent2"], outline="", width=0)

            self.create_text(
                new_width - 10, y + dline[3] // 2,
                anchor="e",
                text=str(linenum),
                fill=C["accent"] if is_current else C["text_soft"],
                font=(MONO_FAMILY, 10, "bold" if is_current else "normal"),
            )
            i = f"{linenum + 1}.0"
            if self.text_widget.compare(i, ">", "end"):
                break


# ══════════════════════════════════════════════════════════════════════════════
class CompilerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.current_lang = "EN"
        self._build_window()
        self._apply_styles()
        self._build_ui()
        self._refresh_lang()
        self.load_sample_code()

    # ── Window setup ──────────────────────────────────────────────────────────
    def _build_window(self):
        self.root.title("Two-Pass Compiler")
        self.root.geometry("1280x780")
        self.root.minsize(900, 600)
        self.root.configure(bg=C["bg"])
        try:
            self.root.state("zoomed")          # Windows maximise
        except Exception:
            pass

    # ── ttk Styles ────────────────────────────────────────────────────────────
    def _apply_styles(self):
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        # ── Notebook ──────────────────────────────────────────────────────────
        style.configure("Modern.TNotebook",
                        background=C["bg"],
                        borderwidth=0,
                        tabmargins=[0, 0, 0, 0])
        style.configure("Modern.TNotebook.Tab",
                        font=(FONT_FAMILY, 10, "bold"),
                        padding=[18, 10],
                        background=C["sidebar"],
                        foreground=C["text_soft"],
                        borderwidth=0,
                        focuscolor=C["accent"])
        style.map("Modern.TNotebook.Tab",
                  background=[("selected", C["panel"]), ("active", C["btn2_hover"])],
                  foreground=[("selected", C["accent"]), ("active", C["text"])],
                  expand=[("selected", [0, 0, 0, 0])])

        # ── Treeview ──────────────────────────────────────────────────────────
        style.configure("Modern.Treeview",
                        background=C["panel"],
                        foreground=C["text"],
                        fieldbackground=C["panel"],
                        rowheight=32,
                        font=(FONT_FAMILY, 10),
                        borderwidth=0,
                        relief="flat")
        style.configure("Modern.Treeview.Heading",
                        background=C["header_bg"],
                        foreground=C["accent"],
                        font=(FONT_FAMILY, 10, "bold"),
                        relief="flat",
                        borderwidth=0,
                        padding=[8, 6])
        style.map("Modern.Treeview",
                  background=[("selected", C["accent2"])],
                  foreground=[("selected", "#FFFFFF")])
        style.map("Modern.Treeview.Heading",
                  background=[("active", C["border"])])

        # ── Scrollbar ─────────────────────────────────────────────────────────
        style.configure("Thin.Vertical.TScrollbar",
                        gripcount=0,
                        background=C["scrollbar"],
                        darkcolor=C["scrollbar"],
                        lightcolor=C["scrollbar"],
                        troughcolor=C["surface"],
                        bordercolor=C["surface"],
                        arrowcolor=C["accent"],
                        width=8)
        style.configure("Thin.Horizontal.TScrollbar",
                        gripcount=0,
                        background=C["scrollbar"],
                        troughcolor=C["surface"],
                        arrowcolor=C["accent"],
                        width=8)

    # ── UI Construction ───────────────────────────────────────────────────────
    def _build_ui(self):
        self._build_header()
        self._build_body()
        self._build_statusbar()

    # ── Header ────────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self.root, bg=C["accent"], height=64)
        hdr.pack(fill=tk.X, side=tk.TOP)
        hdr.pack_propagate(False)

        inner = tk.Frame(hdr, bg=C["accent"])
        inner.pack(fill=tk.BOTH, expand=True, padx=20)

        # dot decorations
        dot_frame = tk.Frame(inner, bg=C["accent"])
        dot_frame.pack(side=tk.LEFT, padx=(0, 14), pady=18)
        for col in ["#FF6B6B", "#FFD93D", "#6BCB77"]:
            tk.Frame(dot_frame, bg=col, width=10, height=10,
                     bd=0, relief="flat").pack(side=tk.LEFT, padx=3)

        title_block = tk.Frame(inner, bg=C["accent"])
        title_block.pack(side=tk.LEFT)

        self.lbl_title = tk.Label(title_block, bg=C["accent"], fg="#FFFFFF",
                                   font=(FONT_FAMILY, 15, "bold"))
        self.lbl_title.pack(anchor="w")
        self.lbl_subtitle = tk.Label(title_block, bg=C["accent"], fg=C["accent2"],
                                      font=(FONT_FAMILY, 9))
        self.lbl_subtitle.pack(anchor="w")

        # Language toggle (top-right)
        self.btn_lang = tk.Button(inner, bd=0, relief="flat",
                                   bg=C["accent2"], fg="#FFFFFF",
                                   activebackground=C["btn_hover"],
                                   activeforeground="#FFFFFF",
                                   font=(FONT_FAMILY, 9, "bold"),
                                   padx=12, pady=6,
                                   cursor="hand2",
                                   command=self.toggle_lang)
        self.btn_lang.pack(side=tk.RIGHT, pady=14)

    # ── Body ──────────────────────────────────────────────────────────────────
    def _build_body(self):
        body = tk.Frame(self.root, bg=C["bg"])
        body.pack(fill=tk.BOTH, expand=True, padx=12, pady=10)

        self._build_left(body)
        self._build_right(body)

    # ── Left Pane ─────────────────────────────────────────────────────────────
    def _build_left(self, parent):
        left = tk.Frame(parent, bg=C["sidebar"], bd=0)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=False,
                  padx=(0, 8), ipadx=0)
        left.configure(width=420)
        left.pack_propagate(False)

        # Editor header
        editor_hdr = tk.Frame(left, bg=C["sidebar"])
        editor_hdr.pack(fill=tk.X, padx=16, pady=(14, 6))

        self.lbl_source = tk.Label(editor_hdr, bg=C["sidebar"], fg=C["text"],
                                    font=(FONT_FAMILY, 11, "bold"))
        self.lbl_source.pack(side=tk.LEFT)

        # line-number label (decorative)
        self.lbl_linecol = tk.Label(editor_hdr, bg=C["sidebar"],
                                     fg=C["text_soft"],
                                     font=(FONT_FAMILY, 9))
        self.lbl_linecol.pack(side=tk.RIGHT)

        # Editor wrapper — outer border frame
        ed_wrap = tk.Frame(left, bg=C["border"], bd=1)
        ed_wrap.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 10))

        # Inner frame holds line-numbers + text side by side
        ed_inner = tk.Frame(ed_wrap, bg=C["editor_bg"])
        ed_inner.pack(fill=tk.BOTH, expand=True)

        # ── Text widget (created first so LineNumbers can reference it) ───────
        self.code_input = tk.Text(
            ed_inner,
            bg=C["editor_bg"], fg=C["editor_fg"],
            insertbackground=C["accent"],
            selectbackground=C["accent2"], selectforeground="#fff",
            font=(MONO_FAMILY, 11),
            relief="flat", bd=0,
            wrap=tk.NONE,
            padx=10, pady=10,
            undo=True,
        )

        # Vertical scrollbar (shared between text and line numbers)
        vsb_editor = ttk.Scrollbar(ed_inner, orient="vertical",
                                    command=self._editor_yview,
                                    style="Thin.Vertical.TScrollbar")
        hsb_editor = ttk.Scrollbar(ed_wrap, orient="horizontal",
                                    command=self.code_input.xview,
                                    style="Thin.Horizontal.TScrollbar")

        self.code_input.configure(
            yscrollcommand=self._editor_yscroll,
            xscrollcommand=hsb_editor.set,
        )

        # ── Line numbers canvas ───────────────────────────────────────────────
        self.line_numbers = LineNumbers(ed_inner, self.code_input)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.code_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb_editor.pack(side=tk.RIGHT, fill=tk.Y)
        hsb_editor.pack(side=tk.BOTTOM, fill=tk.X)

        self.code_input.bind("<KeyRelease>",  self._on_editor_key)
        self.code_input.bind("<ButtonRelease>", self._on_editor_key)
        # Redirect mousewheel on line-number canvas to the text widget
        self.line_numbers.bind("<MouseWheel>",
                                lambda e: self.code_input.event_generate("<MouseWheel>", delta=e.delta))
        self.line_numbers.bind("<Button-4>",
                                lambda e: self.code_input.yview_scroll(-1, "units"))
        self.line_numbers.bind("<Button-5>",
                                lambda e: self.code_input.yview_scroll(1, "units"))

        # Demo selector
        demo_row = tk.Frame(left, bg=C["sidebar"])
        demo_row.pack(fill=tk.X, padx=14, pady=(0, 8))

        self.lbl_demo = tk.Label(demo_row, bg=C["sidebar"], fg=C["text_soft"],
                                 font=(FONT_FAMILY, 9))
        self.lbl_demo.pack(side=tk.LEFT, padx=(0, 6))

        self.demo_var = tk.StringVar()
        self.demo_combo = ttk.Combobox(
            demo_row,
            textvariable=self.demo_var,
            state="readonly",
            width=24,
            font=(FONT_FAMILY, 9),
        )
        self.demo_combo.pack(side=tk.LEFT, padx=(0, 8))
        self.demo_combo.bind("<<ComboboxSelected>>", self._on_demo_selected)

        # Button row
        btn_row = tk.Frame(left, bg=C["sidebar"])
        btn_row.pack(fill=tk.X, padx=14, pady=(0, 14))

        self.btn_sample = self._make_secondary_btn(btn_row, command=self.load_sample_code)
        self.btn_sample.pack(side=tk.LEFT, padx=(0, 8))

        self.btn_clear = self._make_secondary_btn(btn_row, command=self.clear_code)
        self.btn_clear.pack(side=tk.LEFT, padx=(0, 8))

        self.btn_analyze = self._make_primary_btn(btn_row, command=self.analyze_code)
        self.btn_analyze.pack(side=tk.RIGHT)

    def _editor_yview(self, *args):
        """Scrollbar → text widget (line numbers follow via redraw)."""
        self.code_input.yview(*args)
        self.line_numbers.redraw()

    def _editor_yscroll(self, first, last):
        """Text widget → scrollbar + line numbers."""
        # find the scrollbar widget attached to ed_inner
        self.code_input.master.children  # just to touch the frame
        for w in self.code_input.master.winfo_children():
            if isinstance(w, ttk.Scrollbar) and w.cget("orient") == "vertical":
                w.set(first, last)
                break
        self.line_numbers.redraw()

    def _on_editor_key(self, *_):
        self._update_cursor_label()
        self.line_numbers.redraw()

    def _make_primary_btn(self, parent, command):
        btn = tk.Button(parent,
                        bd=0, relief="flat",
                        bg=C["accent"], fg=C["accent_fg"],
                        activebackground=C["btn_hover"],
                        activeforeground="#fff",
                        font=(FONT_FAMILY, 10, "bold"),
                        padx=18, pady=8,
                        cursor="hand2",
                        command=command)
        btn.bind("<Enter>", lambda e: btn.configure(bg=C["btn_hover"]))
        btn.bind("<Leave>", lambda e: btn.configure(bg=C["accent"]))
        return btn

    def _make_secondary_btn(self, parent, command):
        btn = tk.Button(parent,
                        bd=0, relief="flat",
                        bg=C["btn2_bg"], fg=C["text"],
                        activebackground=C["btn2_hover"],
                        activeforeground=C["text"],
                        font=(FONT_FAMILY, 10),
                        padx=14, pady=8,
                        cursor="hand2",
                        command=command)
        btn.bind("<Enter>", lambda e: btn.configure(bg=C["btn2_hover"]))
        btn.bind("<Leave>", lambda e: btn.configure(bg=C["btn2_bg"]))
        return btn

    # ── Right Pane ────────────────────────────────────────────────────────────
    def _build_right(self, parent):
        right = tk.Frame(parent, bg=C["bg"])
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(right, style="Modern.TNotebook")
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tab frames
        self.token_frame  = tk.Frame(self.notebook, bg=C["panel"])
        self.symbol_frame = tk.Frame(self.notebook, bg=C["panel"])
        self.ast_frame    = tk.Frame(self.notebook, bg=C["panel"])
        self.error_frame  = tk.Frame(self.notebook, bg=C["panel"])
        self.guide_frame  = tk.Frame(self.notebook, bg=C["panel"])

        for frame in (self.token_frame, self.symbol_frame,
                      self.ast_frame, self.error_frame, self.guide_frame):
            self.notebook.add(frame, text="…")

        self._build_token_tab()
        self._build_symbol_tab()
        self._build_ast_tab()
        self._build_error_tab()
        self._build_guide_tab()

    # ── Token Tab ─────────────────────────────────────────────────────────────
    def _build_token_tab(self):
        cols = ("line", "type", "value")
        self.token_table = ttk.Treeview(self.token_frame, columns=cols,
                                         show="headings",
                                         style="Modern.Treeview",
                                         selectmode="browse")
        for cid, w in zip(cols, [70, 190, 240]):
            self.token_table.column(cid, width=w, minwidth=50, anchor="center")

        vsb = ttk.Scrollbar(self.token_frame, orient="vertical",
                             command=self.token_table.yview,
                             style="Thin.Vertical.TScrollbar")
        self.token_table.configure(yscrollcommand=vsb.set)

        self.token_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        vsb.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 8), pady=10)

        self.token_table.tag_configure("even", background=C["row_even"])
        self.token_table.tag_configure("odd",  background=C["row_odd"])

    # ── Symbol Tab ────────────────────────────────────────────────────────────
    def _build_symbol_tab(self):
        cols = ("name", "type", "scope", "memory", "line", "value")
        self.symbol_table_view = ttk.Treeview(self.symbol_frame, columns=cols,
                                               show="headings",
                                               style="Modern.Treeview",
                                               selectmode="browse")
        widths = [120, 100, 100, 130, 70, 120]
        for cid, w in zip(cols, widths):
            self.symbol_table_view.column(cid, width=w, minwidth=50, anchor="center")

        vsb = ttk.Scrollbar(self.symbol_frame, orient="vertical",
                             command=self.symbol_table_view.yview,
                             style="Thin.Vertical.TScrollbar")
        self.symbol_table_view.configure(yscrollcommand=vsb.set)

        self.symbol_table_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                                     padx=(10, 0), pady=10)
        vsb.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 8), pady=10)

        self.symbol_table_view.tag_configure("even", background=C["row_even"])
        self.symbol_table_view.tag_configure("odd",  background=C["row_odd"])

    # ── AST Tab ───────────────────────────────────────────────────────────────
    def _build_ast_tab(self):
        self.ast_output = tk.Text(
            self.ast_frame,
            bg=C["editor_bg"], fg=C["text"],
            insertbackground=C["accent"],
            selectbackground=C["accent2"], selectforeground="#fff",
            font=(MONO_FAMILY, 10),
            relief="flat", bd=0,
            padx=16, pady=14,
            wrap=tk.NONE,
            state=tk.DISABLED,
        )
        vsb = ttk.Scrollbar(self.ast_frame, orient="vertical",
                             command=self.ast_output.yview,
                             style="Thin.Vertical.TScrollbar")
        hsb = ttk.Scrollbar(self.ast_frame, orient="horizontal",
                             command=self.ast_output.xview,
                             style="Thin.Horizontal.TScrollbar")
        self.ast_output.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=10, padx=(0, 8))
        hsb.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0, 8))
        self.ast_output.pack(fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 0))

    # ── Error Tab ─────────────────────────────────────────────────────────────
    def _build_error_tab(self):
        self.error_output = tk.Text(
            self.error_frame,
            bg=C["editor_bg"], fg=C["text"],
            insertbackground=C["accent"],
            selectbackground=C["accent2"], selectforeground="#fff",
            font=(FONT_FAMILY, 10),
            relief="flat", bd=0,
            padx=16, pady=14,
            state=tk.DISABLED,
        )
        vsb = ttk.Scrollbar(self.error_frame, orient="vertical",
                             command=self.error_output.yview,
                             style="Thin.Vertical.TScrollbar")
        self.error_output.configure(yscrollcommand=vsb.set)

        # Color tags
        self.error_output.tag_configure("section",
                                         font=(FONT_FAMILY, 10, "bold"),
                                         foreground=C["accent"])
        self.error_output.tag_configure("lex",   foreground=C["warning"])
        self.error_output.tag_configure("syn",   foreground=C["error"])
        self.error_output.tag_configure("sem",   foreground="#9B59B6")
        self.error_output.tag_configure("ok",    foreground=C["success"],
                                         font=(FONT_FAMILY, 11, "bold"))

        vsb.pack(side=tk.RIGHT, fill=tk.Y, pady=10, padx=(0, 8))
        self.error_output.pack(fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)

    def _build_guide_tab(self):
        guide_inner = tk.Frame(self.guide_frame, bg=C["panel"])
        guide_inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        guide_table_frame = tk.Frame(guide_inner, bg=C["panel"])
        guide_table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        cols = ("syntax", "type", "desc")
        self.guide_table = ttk.Treeview(
            guide_table_frame,
            columns=cols,
            show="headings",
            style="Modern.Treeview",
            selectmode="browse",
            height=12,
        )

        for cid, width in zip(cols, [230, 150, 230]):
            self.guide_table.column(cid, width=width, minwidth=90, anchor="center")

        vsb = ttk.Scrollbar(
            guide_table_frame,
            orient="vertical",
            command=self.guide_table.yview,
            style="Thin.Vertical.TScrollbar",
        )
        self.guide_table.configure(yscrollcommand=vsb.set)

        self.guide_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.guide_table.tag_configure("even", background=C["row_even"])
        self.guide_table.tag_configure("odd",  background=C["row_odd"])

        self.tips_title = tk.Label(
            guide_inner,
            bg=C["panel"],
            fg=C["accent"],
            font=(FONT_FAMILY, 12, "bold"),
            anchor="w",
        )
        self.tips_title.pack(fill=tk.X, pady=(18, 8))

        tips_table_frame = tk.Frame(guide_inner, bg=C["panel"])
        tips_table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        tip_cols = ("command", "usage")
        self.tips_table = ttk.Treeview(
            tips_table_frame,
            columns=tip_cols,
            show="headings",
            style="Modern.Treeview",
            selectmode="browse",
            height=7,
        )
        self.tips_table.column("command", width=260, minwidth=120, anchor="center")
        self.tips_table.column("usage", width=520, minwidth=220, anchor="w")
        self.tips_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tips_table.tag_configure("even", background=C["row_even"])
        self.tips_table.tag_configure("odd",  background=C["row_odd"])

        self._populate_guide_table()

    def _populate_guide_table(self):
        for row in self.guide_table.get_children():
            self.guide_table.delete(row)

        for i, row in enumerate(GUIDE_ROWS[self.current_lang]):
            tag = "even" if i % 2 == 0 else "odd"
            self.guide_table.insert("", tk.END, values=row, tags=(tag,))

        for row in self.tips_table.get_children():
            self.tips_table.delete(row)

        for i, row in enumerate(GUIDE_TIPS[self.current_lang]):
            tag = "even" if i % 2 == 0 else "odd"
            self.tips_table.insert("", tk.END, values=row, tags=(tag,))

    # ── Status Bar ────────────────────────────────────────────────────────────
    def _build_statusbar(self):
        bar = tk.Frame(self.root, bg=C["status_bg"], height=28)
        bar.pack(fill=tk.X, side=tk.BOTTOM)
        bar.pack_propagate(False)

        self.status_dot = tk.Label(bar, text="●", bg=C["status_bg"],
                                    fg=C["success"], font=(FONT_FAMILY, 9))
        self.status_dot.pack(side=tk.LEFT, padx=(14, 4))

        self.status_label = tk.Label(bar, bg=C["status_bg"], fg=C["text_soft"],
                                      font=(FONT_FAMILY, 9))
        self.status_label.pack(side=tk.LEFT)

        self.status_right = tk.Label(bar, text="Two-Pass Compiler  v1.0",
                                      bg=C["status_bg"], fg=C["text_soft"],
                                      font=(FONT_FAMILY, 9))
        self.status_right.pack(side=tk.RIGHT, padx=14)

    # ── Language ──────────────────────────────────────────────────────────────
    def toggle_lang(self):
        selected_key = self._selected_demo_key()
        self.current_lang = "TR" if self.current_lang == "EN" else "EN"
        self._refresh_lang(selected_key)

    def _t(self, key):
        return LANG[self.current_lang][key]

    def _demo_labels(self):
        return [LANG[self.current_lang][key] for key in DEMO_KEYS]

    def _selected_demo_key(self):
        label = self.demo_var.get()
        labels = self._demo_labels()
        if label in labels:
            return DEMO_KEYS[labels.index(label)]
        return DEMO_KEYS[0]

    def _refresh_lang(self, selected_demo_key=None):
        L = self.current_lang

        self.lbl_title.config(text=LANG[L]["title"])
        self.lbl_subtitle.config(text=LANG[L]["subtitle"])
        self.btn_lang.config(text=LANG[L]["lang_btn"])
        self.lbl_source.config(text=LANG[L]["source_code"])
        self.lbl_demo.config(text=LANG[L]["demo_label"])
        selected_key = selected_demo_key or self._selected_demo_key()
        self.demo_combo.config(values=self._demo_labels())
        self.demo_var.set(LANG[L][selected_key])
        self.btn_sample.config(text=LANG[L]["load_sample"])
        self.btn_clear.config(text=LANG[L]["clear"])
        self.btn_analyze.config(text=LANG[L]["analyze"])
        self.status_label.config(text=LANG[L]["ready"])

        # Notebook tabs
        for idx, key in enumerate(["tab_tokens", "tab_symbols", "tab_ast", "tab_errors", "tab_guide"]):
            self.notebook.tab(idx, text=LANG[L][key])

        # Treeview headings – token table
        for col, key in [("line", "col_line"), ("type", "col_type"), ("value", "col_value")]:
            self.token_table.heading(col, text=LANG[L][key])

        # Treeview headings – symbol table
        for col, key in [("name", "col_name"), ("type", "col_type"),
                         ("scope", "col_scope"), ("memory", "col_memory"),
                         ("line", "col_line")]:
            self.symbol_table_view.heading(col, text=LANG[L][key])
        self.symbol_table_view.heading("value", text=LANG[L]["col_stored"])

        for col, key in [("syntax", "col_syntax"), ("type", "col_assembly"), ("desc", "col_desc")]:
            self.guide_table.heading(col, text=LANG[L][key])
        self.tips_title.config(text=LANG[L]["tips_title"])
        for col, key in [("command", "col_command"), ("usage", "col_usage")]:
            self.tips_table.heading(col, text=LANG[L][key])
        self._populate_guide_table()

    # ── Core Actions ──────────────────────────────────────────────────────────
    def _on_demo_selected(self, *_):
        self.load_sample_code()

    def load_sample_code(self):
        self.code_input.delete("1.0", tk.END)
        self.code_input.insert(tk.END, DEMO_CODES[self._selected_demo_key()])
        self._update_cursor_label()
        self.after_idle_redraw()

    def clear_code(self):
        self.code_input.delete("1.0", tk.END)
        self._clear_outputs()
        self._update_cursor_label()
        self.after_idle_redraw()

    def after_idle_redraw(self):
        self.root.after_idle(self.line_numbers.redraw)

    def _update_cursor_label(self, *_):
        pos = self.code_input.index(tk.INSERT)
        row, col = pos.split(".")
        self.lbl_linecol.config(text=f"Ln {row}  Col {int(col)+1}")

    def _set_status(self, key, color=None):
        self.status_label.config(text=self._t(key))
        if color:
            self.status_dot.config(fg=color)

    def _clear_outputs(self):
        for tv in (self.token_table, self.symbol_table_view):
            for row in tv.get_children():
                tv.delete(row)
        self._set_text(self.ast_output, "")
        self._set_text(self.error_output, "")

    def _set_text(self, widget, text):
        widget.configure(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        if text:
            widget.insert(tk.END, text)
        widget.configure(state=tk.DISABLED)

    # ── Analyze ───────────────────────────────────────────────────────────────
    def analyze_code(self):
        self._set_status("analyzing", C["warning"])
        self.root.update_idletasks()
        self._clear_outputs()

        try:
            from lexer import tokenize
            from symbol_table import SymbolTable
            from semantic_analyzer import SemanticAnalyzer
            from parser import Parser
        except ImportError as e:
            self._set_text(self.error_output,
                           f"Import error: {e}\nMake sure all compiler modules are present.")
            self._set_status("ready", C["error"])
            return

        source_code = self.code_input.get("1.0", tk.END)

        tokens, lexical_errors = tokenize(source_code)
        effective_tokens = self._tokens_until_stop(tokens)
        symbol_table = SymbolTable()
        semantic_errors = []

        i = 0
        scope_stack = ["global"]
        while i < len(effective_tokens):
            tok = effective_tokens[i]

            if tok["type"] == "KEYWORD" and tok["value"] in ["THIS", "OR", "WHEN", "CYC"]:
                scope_stack.append(tok["value"])

            if tok["type"] == "DELIMITER" and tok["value"] == "}":
                if len(scope_stack) > 1:
                    scope_stack.pop()

            current_scope = scope_stack[-1]

            if tok["type"] == "KEYWORD" and tok["value"] in ["NAT", "COMMA", "TWINAT", "TWINCO"]:
                if i + 1 < len(effective_tokens) and effective_tokens[i + 1]["type"] == "IDENTIFIER":
                    err = symbol_table.add_symbol(
                        effective_tokens[i + 1]["value"],
                        tok["value"],
                        current_scope,
                        effective_tokens[i + 1]["line"]
                    )
                    if err:
                        semantic_errors.append(err)

            i += 1

        self._handle_take_inputs(effective_tokens, symbol_table, semantic_errors)
        semantic_errors.extend(SemanticAnalyzer(effective_tokens, symbol_table).analyze())
        self._apply_runtime_values(effective_tokens, symbol_table)
        ast, syntax_errors = Parser(effective_tokens).parse()

        self._display_tokens(tokens)
        self._display_symbol_table(symbol_table.display())
        self._set_text(self.ast_output, ast.display())
        self._display_errors(lexical_errors, syntax_errors, semantic_errors)

        has_err = any([lexical_errors, syntax_errors, semantic_errors])
        self._set_status("done", C["error"] if has_err else C["success"])

    def _tokens_until_stop(self, tokens):
        effective_tokens = []
        include_stop_semicolon = False
        for token in tokens:
            effective_tokens.append(token)
            if include_stop_semicolon:
                break
            if token["type"] == "KEYWORD" and token["value"] == "STOP":
                include_stop_semicolon = True
        return effective_tokens

    def _handle_take_inputs(self, tokens, symbol_table, semantic_errors):
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token["type"] == "KEYWORD" and token["value"] == "TAKE":
                prompt_token = None
                if (
                    i + 2 < len(tokens)
                    and tokens[i + 1]["type"] == "OPERATOR"
                    and tokens[i + 1]["value"] == "<-"
                ):
                    prompt_token = tokens[i + 2]

                if prompt_token is None:
                    i += 1
                    continue

                prompt = prompt_token["value"]
                target_name = self._find_take_target(prompt_token, symbol_table)
                if target_name is None:
                    semantic_errors.append(
                        f"Line {token['line']}: TAKE prompt must reference a declared variable"
                    )
                    i += 1
                    continue

                symbol = symbol_table.lookup(target_name)
                entered_value = simpledialog.askstring("TAKE", prompt, parent=self.root)
                if entered_value is None:
                    semantic_errors.append(
                        f"Line {token['line']}: TAKE input for '{target_name}' was cancelled"
                    )
                    i += 1
                    continue

                converted_value = self._convert_take_value(entered_value, symbol, token["line"], semantic_errors)
                if converted_value is not None:
                    symbol_table.set_value(target_name, converted_value)

            i += 1

    def _find_take_target(self, prompt_token, symbol_table):
        if prompt_token["type"] == "IDENTIFIER" and symbol_table.lookup(prompt_token["value"]):
            return prompt_token["value"]

        words = str(prompt_token["value"]).replace(":", " ").replace(",", " ").split()
        for word in reversed(words):
            if symbol_table.lookup(word):
                return word
        return None

    def _convert_take_value(self, value, symbol, line, semantic_errors):
        data_type = symbol["type"]
        try:
            if data_type == "NAT":
                return str(int(value))
            if data_type in ["COMMA", "TWINCO"]:
                return str(float(value))
            if data_type == "TWINAT":
                return str(int(value))
        except ValueError:
            semantic_errors.append(
                f"Line {line}: TAKE value '{value}' is not valid for {data_type} variable '{symbol['name']}'"
            )
            return None

        return value

    # ── Display helpers ───────────────────────────────────────────────────────
    def _apply_runtime_values(self, tokens, symbol_table):
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token["type"] == "IDENTIFIER" and i + 1 < len(tokens):
                next_token = tokens[i + 1]

                if next_token["type"] == "DELIMITER" and next_token["value"] == "[":
                    end = self._find_expression_end(tokens, i + 2, "]")
                    if end is not None:
                        value = self._evaluate_expression(tokens[i + 2:end], symbol_table)
                        symbol = symbol_table.lookup(token["value"])
                        if value is not None:
                            symbol_table.set_value(token["value"], self._format_runtime_value(value, symbol))
                        i = end + 1
                        continue

                if next_token["type"] == "OPERATOR" and next_token["value"] == "BY":
                    end = self._find_expression_end(tokens, i + 2, "NEWLINE")
                    if end is not None:
                        value = self._evaluate_expression(tokens[i + 2:end], symbol_table)
                        symbol = symbol_table.lookup(token["value"])
                        if value is not None:
                            symbol_table.set_value(token["value"], self._format_runtime_value(value, symbol))
                        i = end + 1
                        continue

            if token["type"] == "OPERATOR" and token["value"] in ["NEXT", "EX"]:
                if i + 1 < len(tokens) and tokens[i + 1]["type"] == "IDENTIFIER":
                    symbol = symbol_table.lookup(tokens[i + 1]["value"])
                    current_value = self._number_from_symbol(symbol)
                    if current_value is not None:
                        delta = 1 if token["value"] == "NEXT" else -1
                        symbol_table.set_value(symbol["name"], self._format_runtime_value(current_value + delta, symbol))
                    i += 2
                    continue

            i += 1

    def _find_expression_end(self, tokens, start, end_value):
        depth = 0
        for index in range(start, len(tokens)):
            token = tokens[index]
            if token["type"] == "DELIMITER" and token["value"] in ["(", "["]:
                depth += 1
            elif token["type"] == "DELIMITER" and token["value"] in [")", "]"]:
                if depth == 0 and token["value"] == end_value:
                    return index
                depth = max(0, depth - 1)
            elif token["type"] == "DELIMITER" and token["value"] == end_value and depth == 0:
                return index
        if end_value == "NEWLINE":
            return len(tokens)
        return None

    def _evaluate_expression(self, expression_tokens, symbol_table):
        self._runtime_tokens = expression_tokens
        self._runtime_pos = 0
        self._runtime_symbols = symbol_table
        return self._runtime_parse_expression()

    def _runtime_current(self):
        if self._runtime_pos < len(self._runtime_tokens):
            return self._runtime_tokens[self._runtime_pos]
        return None

    def _runtime_advance(self):
        self._runtime_pos += 1

    def _runtime_parse_expression(self):
        left = self._runtime_parse_term()
        while self._runtime_current() is not None:
            token = self._runtime_current()
            if token["type"] == "OPERATOR" and token["value"] in ["PLUS", "MINUS"]:
                self._runtime_advance()
                right = self._runtime_parse_term()
                if left is None or right is None:
                    return None
                left = left + right if token["value"] == "PLUS" else left - right
            else:
                break
        return left

    def _runtime_parse_term(self):
        left = self._runtime_parse_factor()
        while self._runtime_current() is not None:
            token = self._runtime_current()
            if token["type"] == "OPERATOR" and token["value"] in ["BUMP", "CUT"]:
                self._runtime_advance()
                right = self._runtime_parse_factor()
                if left is None or right is None:
                    return None
                left = left * right if token["value"] == "BUMP" else left / right
            else:
                break
        return left

    def _runtime_parse_factor(self):
        token = self._runtime_current()
        if token is None:
            return None

        if token["type"] == "INTEGER_LITERAL":
            self._runtime_advance()
            return int(token["value"])

        if token["type"] == "FLOAT_LITERAL":
            self._runtime_advance()
            return float(token["value"])

        if token["type"] == "IDENTIFIER":
            self._runtime_advance()
            return self._number_from_symbol(self._runtime_symbols.lookup(token["value"]))

        if token["type"] == "OPERATOR" and token["value"] in ["NEXT", "EX"]:
            self._runtime_advance()
            value = self._runtime_parse_factor()
            if value is None:
                return None
            return value + 1 if token["value"] == "NEXT" else value - 1

        if token["type"] == "DELIMITER" and token["value"] == "(":
            self._runtime_advance()
            value = self._runtime_parse_expression()
            if self._runtime_current() is not None and self._runtime_current()["value"] == ")":
                self._runtime_advance()
            return value

        return None

    def _number_from_symbol(self, symbol):
        if symbol is None or symbol.get("value", "") == "":
            return None

        try:
            if symbol["type"] in ["NAT", "TWINAT"]:
                return int(float(symbol["value"]))
            return float(symbol["value"])
        except ValueError:
            return None

    def _format_runtime_value(self, value, symbol=None):
        if symbol is not None and symbol.get("type") in ["COMMA", "TWINCO"]:
            return str(float(value))
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def _display_tokens(self, tokens):
        for row in self.token_table.get_children():
            self.token_table.delete(row)
        for i, tok in enumerate(tokens):
            tag = "even" if i % 2 == 0 else "odd"
            self.token_table.insert("", tk.END,
                                     values=(tok["line"], tok["type"], tok["value"]),
                                     tags=(tag,))

    def _display_symbol_table(self, symbols):
        for row in self.symbol_table_view.get_children():
            self.symbol_table_view.delete(row)
        for i, sym in enumerate(symbols):
            tag = "even" if i % 2 == 0 else "odd"
            self.symbol_table_view.insert("", tk.END,
                                           values=(sym["name"], sym["type"],
                                                   sym["scope"], sym["memory_location"],
                                                   sym["line"], sym.get("value", "")),
                                           tags=(tag,))

    def _display_errors(self, lex_errs, syn_errs, sem_errs):
        w = self.error_output
        w.configure(state=tk.NORMAL)
        w.delete("1.0", tk.END)

        if not lex_errs and not syn_errs and not sem_errs:
            w.insert(tk.END, self._t("no_errors") + "\n", "ok")
        else:
            for label_key, errs, tag in [
                ("lex_errors", lex_errs, "lex"),
                ("syn_errors", syn_errs, "syn"),
                ("sem_errors", sem_errs, "sem"),
            ]:
                if errs:
                    w.insert(tk.END, f"\n  {self._t(label_key)}\n", "section")
                    w.insert(tk.END, "  " + "─" * 40 + "\n", "section")
                    for e in errs:
                        w.insert(tk.END, f"  {e}\n", tag)

        w.configure(state=tk.DISABLED)
        # Switch to errors tab automatically
        self.notebook.select(3)


# ── Entry Point (when run directly) ──────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()
