import axios from 'axios'
import { useEffect, useState } from 'react'
import './menu.css'

interface Burger {
	name: string
	price: number
	description: string
	imageUrl: string
	id: number
}

const Menu = () => {
	const [burgers, setBurgers] = useState<Burger[]>([])
	useEffect(() => {
		axios
			.get('https://66acba11f009b9d5c73331c6.mockapi.io/burgers')
			.then(res => setBurgers(res.data))
			.catch(err => console.log(err))
	}, [])
	return (
		<div className='container'>
			<div className='logo'>
				<img
					src='https://static.tildacdn.com/tild6538-3939-4866-a239-303436613730/photo.svg'
					className='logoImg'
				/>
				<h1 className='logoText'>БУРГЕРЫ</h1>
			</div>
			{burgers?.map((burger: Burger) => (
				<div key={burger.id} className='item'>
					<img src={burger.imageUrl} alt={burger.name} className='image' />
					<h1>{burger.name}</h1>
					<p className='text'>{burger.description}</p>
					<p className='price'>{burger.price} p.</p>
					<button className='button'>Заказать</button>
				</div>
			))}
		</div>
	)
}

export default Menu