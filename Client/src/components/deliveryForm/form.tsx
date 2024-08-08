import { FC } from 'react'
import { useForm, SubmitHandler } from 'react-hook-form'

import style from './form.module.css'

type Inputs = {
	name: string
	email: string
	phone: number
	city: string
	street: string
	house: string
	building: string
	apartment: string
	comment: string
}

type Props = {
	children: JSX.Element
}

const Form: FC<Props> = ({ children }) => {

	const {
		handleSubmit,
		register,
		formState: { errors },
	} = useForm<Inputs>({ mode: 'onSubmit' })

	const onSubmit: SubmitHandler<Inputs> = data => console.log(data)
	
	return (
		<form onSubmit={handleSubmit(onSubmit)} className={style.form}>
			<div>
				<input
					placeholder='Ваше имя'
					{...register('name', { required: true })}
				/>
				{errors.name && <span className={style.error}>Обязательное поле</span>}
			</div>
			<div>
				<input
					placeholder='E-mail'
					{...register('email', { required: true })}
				/>
				{errors.email && <span className={style.error}>Обязательное поле</span>}
			</div>
			<div>
				<input
					placeholder='Ваш телефон'
					{...register('phone', { required: true })}
				/>
				{errors.phone && <span className={style.error}>Обязательное поле</span>}
			</div>
			<div>
				<input placeholder='Город' {...register('city', { required: true })} />
				{errors.city && <span className={style.error}>Обязательное поле</span>}
			</div>
			<div>
				<input
					placeholder='Улица'
					{...register('street', { required: true })}
				/>
				{errors.street && (
					<span className={style.error}>Обязательное поле</span>
				)}
			</div>
			<div>
				<input placeholder='Дом' {...register('house', { required: true })} />
				{errors.house && <span className={style.error}>Обязательное поле</span>}
			</div>
			<div>
				<input
					placeholder='Корпус'
					{...register('building', { required: true })}
				/>
				{errors.building && (
					<span className={style.error}>Обязательное поле</span>
				)}
			</div>
			<div>
				<input
					placeholder='Квартира'
					{...register('apartment', { required: true })}
				/>
				{errors.apartment && (
					<span className={style.error}>Обязательное поле</span>
				)}
			</div>
			<input placeholder='Комментарий' {...register('comment')} />
			{children}
			<button type='submit' className={style.button}>
				Оформить заказ
			</button>
		</form>
	)
}

export default Form
