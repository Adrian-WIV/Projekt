namespace _20250703_datenbank
{
    partial class Form1
    {
        /// <summary>
        /// Erforderliche Designervariable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Verwendete Ressourcen bereinigen.
        /// </summary>
        /// <param name="disposing">True, wenn verwaltete Ressourcen gelöscht werden sollen; andernfalls False.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Vom Windows Form-Designer generierter Code

        /// <summary>
        /// Erforderliche Methode für die Designerunterstützung.
        /// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
        /// </summary>
        private void InitializeComponent()
        {
            this.lb_name = new System.Windows.Forms.Label();
            this.lb_bestellmenge = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.bn_suche = new System.Windows.Forms.Button();
            this.performanceCounter1 = new System.Diagnostics.PerformanceCounter();
            this.lib_daten = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.performanceCounter1)).BeginInit();
            this.SuspendLayout();
            // 
            // lb_name
            // 
            this.lb_name.AutoSize = true;
            this.lb_name.Location = new System.Drawing.Point(79, 59);
            this.lb_name.Name = "lb_name";
            this.lb_name.Size = new System.Drawing.Size(47, 16);
            this.lb_name.TabIndex = 0;
            this.lb_name.Text = "Name:";
            this.lb_name.Click += new System.EventHandler(this.lb_name_Click);
            // 
            // lb_bestellmenge
            // 
            this.lb_bestellmenge.AutoSize = true;
            this.lb_bestellmenge.Location = new System.Drawing.Point(80, 165);
            this.lb_bestellmenge.Name = "lb_bestellmenge";
            this.lb_bestellmenge.Size = new System.Drawing.Size(93, 16);
            this.lb_bestellmenge.TabIndex = 1;
            this.lb_bestellmenge.Text = "Bestellmenge:";
            this.lb_bestellmenge.Click += new System.EventHandler(this.lb_bestellmenge_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(83, 98);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 22);
            this.textBox1.TabIndex = 2;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(82, 224);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 22);
            this.textBox2.TabIndex = 3;
            this.textBox2.TextChanged += new System.EventHandler(this.textBox2_TextChanged);
            // 
            // bn_suche
            // 
            this.bn_suche.Location = new System.Drawing.Point(83, 314);
            this.bn_suche.Name = "bn_suche";
            this.bn_suche.Size = new System.Drawing.Size(84, 43);
            this.bn_suche.TabIndex = 4;
            this.bn_suche.Text = "Suchen";
            this.bn_suche.UseVisualStyleBackColor = true;
            this.bn_suche.Click += new System.EventHandler(this.bn_suche_Click);
            // 
            // lib_daten
            // 
            this.lib_daten.FormattingEnabled = true;
            this.lib_daten.ItemHeight = 16;
            this.lib_daten.Location = new System.Drawing.Point(504, 49);
            this.lib_daten.Name = "lib_daten";
            this.lib_daten.Size = new System.Drawing.Size(261, 212);
            this.lib_daten.TabIndex = 5;
            this.lib_daten.SelectedIndexChanged += new System.EventHandler(this.lib_daten_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.lib_daten);
            this.Controls.Add(this.bn_suche);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.lb_bestellmenge);
            this.Controls.Add(this.lb_name);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.performanceCounter1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_name;
        private System.Windows.Forms.Label lb_bestellmenge;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button bn_suche;
        private System.Diagnostics.PerformanceCounter performanceCounter1;
        private System.Windows.Forms.ListBox lib_daten;
    }
}

