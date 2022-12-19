using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace MortgagePayments
{
    public partial class sign_up : Form
    {
        DB dataBase = new DB();
        protected override void WndProc(ref Message message)
        {
            if (message.Msg == 0x201)
            {
                base.Capture = false;
                message = Message.Create(base.Handle, 0xA1, new IntPtr(2), IntPtr.Zero);
            }
            base.WndProc(ref message);

        }
        public sign_up()
        {
            InitializeComponent();
            StartPosition = FormStartPosition.CenterScreen;
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            this.Close();
        }


        private void pictureBox7_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {

            var loginUser = textBox2.Text;
            var passUser = textBox1.Text;


            string userstring = $"insert into register(login_user,password_user) values ('{loginUser}','{passUser}')";
            SqlCommand command = new SqlCommand(userstring, dataBase.getConnection());
            
            dataBase.openConnection();


            if (command.ExecuteNonQuery() == 1)
            {
                MessageBox.Show("Аккаунт успешно создан", "Успех");
                Registr frm1r = new Registr();
                this.Hide();
                frm1r.ShowDialog();
                this.Close();
            }
            else
            {
                MessageBox.Show("Аккаунт не создан");
            }
            dataBase.closeConnection();
            if (checkuser())

            {
                return;

            }
        }
        private Boolean checkuser()
        {
            var loginUser = textBox2.Text;
            var passUser = textBox1.Text;

            SqlDataAdapter adapter = new SqlDataAdapter();
            DataTable table = new DataTable();
            string userstring = $"select id_user,login_user,password_user from register where login_user = '{loginUser}' and password_user = '{passUser}'";

            SqlCommand command = new SqlCommand(userstring, dataBase.getConnection());

            adapter.SelectCommand = command;
            adapter.Fill(table);
            if(table.Rows.Count > 0)
            {
                MessageBox.Show("Пользователь уже существует");
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}




