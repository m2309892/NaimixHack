import React, { useEffect, useState } from 'react';
import Header from '../../components/Header'
import './table.css'
import InnerUser from './Inner';
import Navbar from '../../components/navbar/Navbar';
import {Table} from 'antd'


const TableGen = () => {
    const [toggle, setToggle] = useState(false);
    const [data, setData] = useState(null);
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);

    // useEffect(() => {
    //     setToggle(true);
    //     const dataF = fetch(`${HOSTURL}/`, {
    //         company_id: 0,
    //     })
    //     .then(res => res.json())
    //     .then(res => setData(res))
    //     .catch(e => console.log(e));

    //     setToggle(false);
    // }, [])

    const onSelectChange = (newSelectedRowKeys) => {
        console.log('selectedRowKeys changed: ', newSelectedRowKeys);
        setSelectedRowKeys(newSelectedRowKeys);
      };

    const rowSelection = {
        selectedRowKeys,
        onChange: onSelectChange,
      };

 
const statusCol = ({ name, vacancy, imgUrl = "./avatar.png" }) => (
    <div className="nameCol">
      <img src={imgUrl} alt="Avatar" />
      <div>
        <p>{name}</p>
        <p>{vacancy}</p>
      </div>
    </div>
  );
  
  const teamsCol = ({ name, imgUrl = "./avatar.png" }) => (
    <div className="teamCol">
      <img src={imgUrl} alt="Avatar" />
      <p>{name}</p>
    </div>
  );
  
  const columns = [
    {
      title: 'Сотрудник',
      dataIndex: 'name',
      key: 'name',
      render: (text, record) => statusCol({ name: record.name, vacancy: record.vacancy, imgUrl: record.imgUrl })
    },
    {
      title: 'Статус',
      dataIndex: 'status',
      key: 'status',
      width: 220,
    },
    {
      title: 'Команда',
      dataIndex: 'team',
      key: 'team',
      width: 258, 
      render: (text, record) => teamsCol({ name: record.teamName, imgUrl: record.teamImgUrl })
    },
  ];
  
  const dataSource = Array.from({ length: 5 }).map((_, i) => ({
    key: i,
    name: 'Herr Muller',
    vacancy: 'UX jobby',
    imgUrl: "./avatar.png",
    status: <div className="status">{_?.job ?? 'Джун'}</div>,
    teamName: 'Партнерская ссылка',
    teamImgUrl: './public/avatar.png',
  }));
    

    return(
        <>
        <Table
            rowSelection={rowSelection} 
            columns={columns} 
            dataSource={dataSource ?? data}
            loading={toggle} 
            style={{width: '100%'}} 
            pagination={false} />
        </>
    )
}


export default TableGen;
