using System;
using System.Collections.Generic;
using System.Text;
using System.Data.SqlClient;


namespace MortgagePayments
{
    class DB
    {
        SqlConnection sqlConnection = new SqlConnection(@"Data Source = DESKTOP-D81L17M;Initial Catalog=user;Integrated Security=True");


        public void openConnection()
        {
            if (sqlConnection.State == System.Data.ConnectionState.Closed)
            {
                sqlConnection.Open();
            }

        }
        public void closeConnection()
        {
            if (sqlConnection.State == System.Data.ConnectionState.Open)
            {
                sqlConnection.Close();
            }

        }
        public SqlConnection getConnection()
        {
            return sqlConnection;

        }

    }
}
