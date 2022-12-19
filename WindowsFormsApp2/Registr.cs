using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace MortgagePayments
{
    public partial class Registr : Form
    {

        DB database = new DB();
        public Registr()
        {
            InitializeComponent();
            StartPosition = FormStartPosition.CenterScreen;
        }

        protected override void WndProc(ref Message message)
        {
            if (message.Msg == 0x201)
            {
                base.Capture = false;
                message = Message.Create(base.Handle, 0xA1, new IntPtr(2), IntPtr.Zero);
            }
            base.WndProc(ref message);
        }
        private void pictureBox6_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Registr_Load(object sender, EventArgs e)
        {
            textBox1.PasswordChar = '•';
            textBox2.MaxLength = 50;
            textBox1.MaxLength = 50;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            sign_up frm_sign = new sign_up();
            this.Hide();
            frm_sign.ShowDialog();
            this.Show();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var loginUser = textBox2.Text;
            var passUser = textBox1.Text;

            SqlDataAdapter adapter = new SqlDataAdapter();
            DataTable table = new DataTable();

            string userstring = $"select id_user,login_user,password_user from register where login_user = '{loginUser}' and password_user = '{passUser}'";
            SqlCommand command = new SqlCommand(userstring, database.getConnection());

            adapter.SelectCommand = command;
            adapter.Fill(table);

            if (table.Rows.Count == 1)
            {
                MessageBox.Show("Вы успешно вошли!", "Успешно", MessageBoxButtons.OK, MessageBoxIcon.Information);
                Form1 frm1 = new Form1();
                this.Hide();
                frm1.ShowDialog();
                this.Show();
                this.Close();
            }
            else
            {
                MessageBox.Show("Такого аккаунта не существует", "Аккаунта не существует ", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            textBox1.UseSystemPasswordChar = true;
            pictureBox4.Visible = true;
            pictureBox5.Visible = false;
        }
        private void pictureBox4_Click(object sender, EventArgs e)
        {
            textBox1.UseSystemPasswordChar = false;
            pictureBox4.Visible = false;
            pictureBox5.Visible = true;
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }
    }
}
