/**
 * MysqlTest.cpp
 *
 * Copyright 2012 Cody Van De Mark
 * 
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either 
 * version 3.0 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this library.  If not, see <http://www.gnu.org/licenses/>.
 * 
 **/

#include <iostream>
#include <mysql++.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	try	
	{
		mysqlpp::Connection conn("forums", "localhost", "root", "dblab");
		mysqlpp::Query query = conn.query("SELECT * FROM threads");
		mysqlpp::StoreQueryResult res = query.store();

		if (res)
		{
			cout.setf(ios::left);
			cout << setw(8) << "Id" << setw(9) << "MessageID" << setw(3) << "threadID" << setw(20) << "dateCreated" << setw(50) << "threadName" << endl << endl;

			for (size_t i = 0; i < res.num_rows(); i++)
			{
			   cout << setw(8) << res[i]["id"] 
				<< ' ' << setw(9) << res[i]["messageID"] 
				<< ' ' << setw(3) << res[i]["threadID"] 
				<< ' ' << setw(20) << res[i]["dateCreated"] 
				<< ' ' << setw(50) << res[i]["threadName"] << endl;
			}
		}
	}
	catch (mysqlpp::ConnectionFailed& e)
	{

	}

	return 0;
}
